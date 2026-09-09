import pytest
import uuid
import logging
from mysql.connector import IntegrityError
from utils.db_utils import DBUtils

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri", database="flight_reservation")
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

@pytest.mark.smoke
def test_booking_records_exist(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM bookings;")
    count = cur.fetchone()[0]
    assert count >= 10
    cur.close()

@pytest.mark.regression
def test_booking_references_unique(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT booking_reference, COUNT(*)
        FROM bookings
        GROUP BY booking_reference
        HAVING COUNT(*) > 1;
    """)
    duplicates = cur.fetchall()
    assert len(duplicates) == 0
    cur.close()

@pytest.mark.regression
def test_booking_has_valid_customer(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.*
        FROM bookings b
        LEFT JOIN customers c ON b.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_booking_has_valid_flight(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.*
        FROM bookings b
        LEFT JOIN flights f ON b.flight_id = f.flight_id
        WHERE f.flight_id IS NULL;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_booking_has_valid_seat(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.*
        FROM bookings b
        LEFT JOIN flight_seats fs ON b.seat_id = fs.seat_id
        WHERE fs.seat_id IS NULL;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_booking_seat_consistency(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.booking_id, b.flight_id AS booking_flight, fs.flight_id AS seat_flight
        FROM bookings b
        JOIN flight_seats fs ON b.seat_id = fs.seat_id
        WHERE b.flight_id <> fs.flight_id;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_valid_booking_statuses(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT * FROM bookings
        WHERE booking_status NOT IN ('PENDING','CONFIRMED','CANCELLED');
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_booking_amounts(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM bookings WHERE total_amount <= 0;")
    invalid = cur.fetchall()
    assert len(invalid) == 0

    # Negative insert
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO bookings (booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount)
            VALUES ('NEGTEST',1,1,1,NOW(),'PENDING',-100);
        """)
        db_connection.commit()
    cur.close()

@pytest.mark.regression
def test_create_and_confirm_booking(db_connection):
    cur = db_connection.cursor()

    # Step 1: Find customer
    cur.execute("SELECT customer_id FROM customers LIMIT 1;")
    customer_id = cur.fetchone()[0]

    # Step 2: Find flight
    cur.execute("SELECT flight_id FROM flights WHERE status='SCHEDULED' LIMIT 1;")
    flight_id = cur.fetchone()[0]

    # Step 3: Find available seat
    cur.execute("SELECT seat_id, seat_number FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE' LIMIT 1;", (flight_id,))
    seat = cur.fetchone()
    assert seat is not None, "No available seat found"
    seat_id, seat_number = seat

    logging.info(f"Customer selected: {customer_id}, Flight: {flight_id}, Seat: {seat_number}")

    # Step 4: Create booking
    booking_reference = f"TEST{uuid.uuid4().hex[:8].upper()}"
    total_amount = 5000
    cur.execute("""
        INSERT INTO bookings (booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount)
        VALUES (%s,%s,%s,%s,NOW(),'PENDING',%s);
    """, (booking_reference, customer_id, flight_id, seat_id, total_amount))
    db_connection.commit()
    booking_id = cur.lastrowid

    # Step 5: Verify booking
    cur.execute("SELECT booking_status, total_amount FROM bookings WHERE booking_reference=%s;", (booking_reference,))
    status, amount = cur.fetchone()
    assert status == "PENDING"
    assert amount == total_amount

    # Step 6: Update seat to BOOKED
    cur.execute("UPDATE flight_seats SET seat_status='BOOKED' WHERE seat_id=%s AND seat_status='AVAILABLE';", (seat_id,))
    db_connection.commit()
    assert cur.rowcount == 1
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    seat_status = cur.fetchone()[0]
    assert seat_status == "BOOKED"

    # Step 7: Update booking to CONFIRMED
    cur.execute("UPDATE bookings SET booking_status='CONFIRMED' WHERE booking_id=%s;", (booking_id,))
    db_connection.commit()
    cur.execute("SELECT booking_status FROM bookings WHERE booking_id=%s;", (booking_id,))
    new_status = cur.fetchone()[0]
    assert new_status == "CONFIRMED"

    logging.info(f"Booking {booking_reference} confirmed with seat {seat_number}")

    # Cleanup: delete booking and restore seat
    try:
        cur.execute("DELETE FROM bookings WHERE booking_id=%s;", (booking_id,))
        cur.execute("UPDATE flight_seats SET seat_status='AVAILABLE' WHERE seat_id=%s;", (seat_id,))
        db_connection.commit()
    finally:
        cur.close()

@pytest.mark.regression
def test_booking_transaction_rollback(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT customer_id FROM customers LIMIT 1;")
    customer_id = cur.fetchone()[0]
    cur.execute("SELECT flight_id FROM flights WHERE status='SCHEDULED' LIMIT 1;")
    flight_id = cur.fetchone()[0]
    cur.execute("SELECT seat_id FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE' LIMIT 1;", (flight_id,))
    seat = cur.fetchone()
    assert seat is not None
    seat_id = seat[0]

    booking_reference = f"ROLL{uuid.uuid4().hex[:8].upper()}"
    db_connection.start_transaction()
    try:
        cur.execute("""
            INSERT INTO bookings (booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount)
            VALUES (%s,%s,%s,%s,NOW(),'PENDING',1000);
        """, (booking_reference, customer_id, flight_id, seat_id))
        cur.execute("UPDATE flight_seats SET seat_status='BOOKED' WHERE seat_id=%s;", (seat_id,))
        cur.execute("""
            INSERT INTO passengers (booking_id, first_name, last_name, passport_number, date_of_birth)
            VALUES (999999,'Test','Fail','X12345','2000-01-01');
        """)  # invalid booking_id to force failure
        db_connection.commit()
    except Exception:
        db_connection.rollback()

    # Verify rollback
    cur.execute("SELECT * FROM bookings WHERE booking_reference=%s;", (booking_reference,))
    assert cur.fetchone() is None
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    status = cur.fetchone()[0]
    assert status == "AVAILABLE"
    cur.close()
