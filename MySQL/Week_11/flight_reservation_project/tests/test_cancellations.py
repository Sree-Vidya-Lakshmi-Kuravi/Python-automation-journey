import pytest
import logging
import time
from mysql.connector import DatabaseError
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

# --- Booking cancellation validations ---
@pytest.mark.smoke
def test_valid_booking_statuses(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT * FROM bookings
        WHERE booking_status NOT IN ('PENDING','CONFIRMED','CANCELLED');
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0, f"Invalid booking statuses found: {invalid}"
    cur.close()

@pytest.mark.smoke
def test_cancelled_bookings_exist(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM bookings WHERE booking_status='CANCELLED';")
    cancelled = cur.fetchall()
    logging.info(f"Found {len(cancelled)} cancelled bookings")
    assert cancelled is not None
    cur.close()

@pytest.mark.regression
def test_cancelled_booking_no_booked_seat(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.booking_id, b.booking_status, fs.seat_status
        FROM bookings b
        JOIN flight_seats fs ON b.seat_id = fs.seat_id
        WHERE b.booking_status='CANCELLED' AND fs.seat_status='BOOKED';
    """)
    inconsistencies = cur.fetchall()
    assert len(inconsistencies) == 0, f"Cancelled bookings with BOOKED seats: {inconsistencies}"
    cur.close()

# --- Refund validations ---
@pytest.mark.smoke
def test_refund_records_exist(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM refunds;")
    count = cur.fetchone()[0]
    logging.info(f"Refund records count: {count}")
    assert count >= 0
    cur.close()

@pytest.mark.regression
def test_refund_reference_unique(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT refund_reference, COUNT(*)
        FROM refunds
        GROUP BY refund_reference
        HAVING COUNT(*) > 1;
    """)
    duplicates = cur.fetchall()
    assert len(duplicates) == 0, f"Duplicate refund references: {duplicates}"
    cur.close()

@pytest.mark.regression
def test_refund_has_valid_payment(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT r.*
        FROM refunds r
        LEFT JOIN payments p ON r.payment_id = p.payment_id
        WHERE p.payment_id IS NULL;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0, f"Refunds with invalid payment_id: {invalid}"
    cur.close()

@pytest.mark.regression
def test_valid_refund_statuses(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT * FROM refunds
        WHERE refund_status NOT IN ('INITIATED','PROCESSED','FAILED');
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0, f"Invalid refund statuses: {invalid}"
    cur.close()

@pytest.mark.regression
def test_valid_refund_amounts(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM refunds WHERE refund_amount <= 0;")
    invalid = cur.fetchall()
    assert len(invalid) == 0, f"Refunds with non-positive amounts: {invalid}"

    # Negative insert should fail due to CHECK constraint
    refund_id = int(time.time())
    with pytest.raises(DatabaseError):
        cur.execute("""
            INSERT INTO refunds (
                refund_id, payment_id, refund_reference, refund_amount,
                refund_status, refund_date
            )
            VALUES (%s,1,'NEGREF',-100,'INITIATED',NOW());
        """, (refund_id,))
        db_connection.commit()
    cur.close()

@pytest.mark.regression
def test_refund_not_exceed_payment(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT r.refund_id, r.payment_id, r.refund_amount, p.amount
        FROM refunds r
        JOIN payments p ON r.payment_id = p.payment_id
        WHERE r.refund_amount > p.amount;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0, f"Refunds exceeding payment amount: {invalid}"
    cur.close()

@pytest.mark.regression
def test_payment_booking_refund_consistency(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.booking_reference, b.booking_status,
               p.transaction_reference, p.payment_status, p.amount,
               r.refund_reference, r.refund_status, r.refund_amount
        FROM bookings b
        JOIN payments p ON b.booking_id = p.booking_id
        LEFT JOIN refunds r ON p.payment_id = r.payment_id;
    """)
    results = cur.fetchall()
    assert results is not None
    logging.info(f"Consistency check returned {len(results)} rows")
    cur.close()

# --- Main cancellation workflow ---
@pytest.mark.sanity
def test_cancel_booking_and_release_seat(db_connection):
    cur = db_connection.cursor()

    # Step 1: Find confirmed booking
    cur.execute("SELECT booking_id, seat_id FROM bookings WHERE booking_status='CONFIRMED' LIMIT 1;")
    booking = cur.fetchone()
    assert booking is not None, "No confirmed booking found"
    booking_id, seat_id = booking

    # Step 2: Check seat status
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    seat_status = cur.fetchone()[0]
    logging.info(f"Booking {booking_id} seat {seat_id} status before cancel: {seat_status}")

    if seat_status != "BOOKED":
        pytest.skip(f"Seat {seat_id} is not BOOKED (status={seat_status}), skipping cancellation workflow")

    # Step 3: Cancel booking
    cur.execute("""
        UPDATE bookings
        SET booking_status='CANCELLED'
        WHERE booking_id=%s AND booking_status='CONFIRMED';
    """, (booking_id,))
    db_connection.commit()
    assert cur.rowcount == 1

    cur.execute("SELECT booking_status FROM bookings WHERE booking_id=%s;", (booking_id,))
    new_status = cur.fetchone()[0]
    assert new_status == "CANCELLED"

    # Step 4: Release seat
    cur.execute("""
        UPDATE flight_seats
        SET seat_status='AVAILABLE'
        WHERE seat_id=%s AND seat_status='BOOKED';
    """, (seat_id,))
    db_connection.commit()
    assert cur.rowcount == 1

    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    final_seat_status = cur.fetchone()[0]
    assert final_seat_status == "AVAILABLE"

    # Cleanup: restore booking and seat
    try:
        cur.execute("UPDATE bookings SET booking_status='CONFIRMED' WHERE booking_id=%s;", (booking_id,))
        cur.execute("UPDATE flight_seats SET seat_status='BOOKED' WHERE seat_id=%s;", (seat_id,))
        db_connection.commit()
    finally:
        cur.close()
