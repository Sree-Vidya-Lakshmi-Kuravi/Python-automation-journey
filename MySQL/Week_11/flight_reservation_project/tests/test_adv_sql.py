import pytest
import logging
from utils.db_utils import DBUtils

logging.basicConfig(level=logging.INFO, format="%(message)s")

@pytest.fixture(scope="module")
def db_connection():
    db = DBUtils(password="siri", database="flight_reservation")
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

# --- Test 1: Rank flights by fare ---
@pytest.mark.smoke
def test_rank_flights_by_fare(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT flight_id, flight_number, base_fare, RANK() OVER (ORDER BY base_fare DESC) AS fare_rank
        FROM flights;
    """)
    rows = cur.fetchall()
    assert rows, "No flights found"
    # highest fare should have rank 1
    max_fare = max(r["base_fare"] for r in rows)
    top_rank = [r for r in rows if r["base_fare"] == max_fare][0]["fare_rank"]
    assert top_rank == 1
    cur.close()

# --- Test 2: Rank flights within each airline ---
@pytest.mark.smoke
def test_rank_flights_within_airline(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT airline_id, flight_id, base_fare, RANK() OVER (PARTITION BY airline_id ORDER BY base_fare DESC) AS fare_rank
        FROM flights;
    """)
    rows = cur.fetchall()
    assert rows
    # validate ranking restarts per airline
    for airline in set(r["airline_id"] for r in rows):
        ranks = [r["fare_rank"] for r in rows if r["airline_id"] == airline]
        assert 1 in ranks
    cur.close()

# --- Test 3: Seat occupancy per flight ---
@pytest.mark.regression
def test_seat_occupancy_per_flight(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT flight_id, COUNT(*) AS total_seats, SUM(CASE WHEN seat_status='BOOKED' THEN 1 ELSE 0 END) AS booked_seats
        FROM flight_seats
        GROUP BY flight_id;
    """)
    rows = cur.fetchall()
    for r in rows:
        assert r["total_seats"] >= r["booked_seats"]
        assert r["booked_seats"] >= 0
        occupancy = (r["booked_seats"] / r["total_seats"]) * 100 if r["total_seats"] else 0
        assert occupancy <= 100
    cur.close()

# --- Test 4: Booking/payment status consistency ---
@pytest.mark.regression
def test_booking_payment_consistency(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT b.booking_id, b.booking_status, p.payment_status, 
        CASE WHEN b.booking_status='CONFIRMED' AND p.payment_status='SUCCESS'
        THEN 'VALID' ELSE 'INVALID' END AS validation_status
        FROM bookings b
        JOIN payments p ON b.booking_id = p.booking_id;
    """)
    rows = cur.fetchall()
    invalids = [r for r in rows if r["validation_status"] == "INVALID"]
    assert len(invalids) == 0, f"Inconsistent booking/payment records: {invalids}"
    cur.close()

# --- Test 5: Booking amount vs payment amount ---
@pytest.mark.regression
def test_booking_amount_vs_payment_amount(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT b.booking_id, b.total_amount, p.amount
        FROM bookings b
        JOIN payments p ON b.booking_id = p.booking_id
        WHERE p.payment_status='SUCCESS';
    """)
    rows = cur.fetchall()
    for r in rows:
        assert r["total_amount"] == r["amount"], f"Mismatch for booking {r['booking_id']}"
    cur.close()

# --- Test 6: Booked seat belongs to correct flight ---
@pytest.mark.regression
def test_booked_seat_belongs_to_correct_flight(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT b.booking_id, b.flight_id AS booking_flight, fs.flight_id AS seat_flight
        FROM bookings b
        JOIN flight_seats fs ON b.seat_id = fs.seat_id
        WHERE b.booking_status IN ('PENDING','CONFIRMED');
    """)
    rows = cur.fetchall()
    inconsistencies = [r for r in rows if r["booking_flight"] != r["seat_flight"]]
    assert len(inconsistencies) == 0, f"Inconsistent booking-seat relationships: {inconsistencies}"
    cur.close()

# --- Test 7: Flights with no available seats ---
@pytest.mark.smoke
def test_flights_with_no_available_seats(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT f.flight_id, f.flight_number
        FROM flights f
        WHERE NOT EXISTS (
            SELECT 1 FROM flight_seats fs
            WHERE fs.flight_id = f.flight_id AND fs.seat_status='AVAILABLE'
        );
    """)
    rows = cur.fetchall()
    for r in rows:
        cur.execute("SELECT COUNT(*) FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE';", (r["flight_id"],))
        count = cur.fetchone()[0]
        assert count == 0
    cur.close()

# --- Test 8: Customers with confirmed bookings ---
@pytest.mark.smoke
def test_customers_with_confirmed_bookings(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT c.customer_id, c.email
        FROM customers c
        WHERE EXISTS (
            SELECT 1 FROM bookings b
            WHERE b.customer_id = c.customer_id AND b.booking_status='CONFIRMED'
        );
    """)
    rows = cur.fetchall()
    for r in rows:
        cur.execute("SELECT COUNT(*) AS cnt FROM bookings WHERE customer_id=%s AND booking_status='CONFIRMED';", (r["customer_id"],))
        count = cur.fetchone()["cnt"]
        assert count > 0
    cur.close()


# --- Test 9: Latest booking/payment using ROW_NUMBER ---
@pytest.mark.regression
def test_latest_payment_per_booking(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        SELECT * FROM (
            SELECT p.*, ROW_NUMBER() OVER (
                PARTITION BY booking_id ORDER BY payment_date DESC
            ) AS rn
            FROM payments p
        ) x WHERE rn=1;
    """)
    rows = cur.fetchall()
    assert rows
    # ensure only one per booking
    seen = set()
    for r in rows:
        assert r["booking_id"] not in seen
        seen.add(r["booking_id"])
    cur.close()

# --- Test 10: Refund consistency using CTE ---
@pytest.mark.regression
def test_refund_consistency(db_connection):
    cur = db_connection.cursor(dictionary=True)
    cur.execute("""
        WITH refund_data AS (
            SELECT p.payment_id, p.amount AS payment_amount, r.refund_amount
            FROM payments p
            JOIN refunds r ON p.payment_id = r.payment_id
        )
        SELECT * FROM refund_data WHERE refund_amount > payment_amount;
    """)
    rows = cur.fetchall()
    assert len(rows) == 0, f"Invalid refunds found: {rows}"
    cur.close()
