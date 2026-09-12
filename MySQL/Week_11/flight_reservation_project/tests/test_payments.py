import pytest
import logging
import time
from mysql.connector import IntegrityError
from utils.db_utils import DBUtils

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

@pytest.fixture(scope="module")
def db_connection():
    db = DBUtils(password="siri", database="flight_reservation")
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

# --- Smoke tests ---
@pytest.mark.smoke
def test_payment_records_exist(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM payments;")
    count = cur.fetchone()[0]
    assert count >= 1
    cur.close()

# --- Regression validations ---
@pytest.mark.regression
def test_transaction_references_unique(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT transaction_reference, COUNT(*)
        FROM payments
        GROUP BY transaction_reference
        HAVING COUNT(*) > 1;
    """)
    duplicates = cur.fetchall()
    assert len(duplicates) == 0
    cur.close()

@pytest.mark.regression
def test_payment_has_valid_booking(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT p.*
        FROM payments p
        LEFT JOIN bookings b ON p.booking_id = b.booking_id
        WHERE b.booking_id IS NULL;
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_valid_payment_statuses(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT * FROM payments
        WHERE payment_status NOT IN ('INITIATED','SUCCESS','FAILED');
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

@pytest.mark.regression
def test_valid_payment_methods(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT * FROM payments
        WHERE payment_method NOT IN ('CARD','UPI','NET_BANKING','WALLET');
    """)
    invalid = cur.fetchall()
    assert len(invalid) == 0
    cur.close()

from mysql.connector import DatabaseError

@pytest.mark.regression
def test_payment_amounts(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM payments WHERE amount <= 0;")
    invalid = cur.fetchall()
    assert len(invalid) == 0

    # Negative insert should fail due to CHECK constraint
    payment_id = int(time.time())
    with pytest.raises(DatabaseError):
        cur.execute("""
            INSERT INTO payments (
                payment_id, booking_id, transaction_reference, amount,
                payment_method, payment_status, payment_date
            )
            VALUES (%s,1,'NEGPMT',-500,'CARD','INITIATED',NOW());
        """, (payment_id,))
        db_connection.commit()
    cur.close()

@pytest.mark.regression
def test_payment_booking_amount_consistency(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT p.payment_id, p.booking_id, p.amount, b.total_amount
        FROM payments p
        JOIN bookings b ON p.booking_id = b.booking_id
        WHERE p.payment_status='SUCCESS' AND p.amount <> b.total_amount;
    """)
    mismatches = cur.fetchall()
    assert len(mismatches) == 0
    cur.close()

# --- Sanity: payment lifecycle ---
@pytest.mark.sanity
def test_create_and_success_payment(db_connection):
    cur = db_connection.cursor()

    # Step 1: Find confirmed booking
    cur.execute("SELECT booking_id, total_amount FROM bookings WHERE booking_status='CONFIRMED' LIMIT 1;")
    booking = cur.fetchone()
    assert booking is not None, "No confirmed booking found"
    booking_id, booking_amount = booking

    # Step 2: Create payment with explicit payment_id
    payment_id = int(time.time())
    txn_ref = f"TXN{payment_id}"
    cur.execute("""
        INSERT INTO payments (
            payment_id, booking_id, transaction_reference, amount,
            payment_method, payment_status, payment_date
        )
        VALUES (%s,%s,%s,%s,'CARD','INITIATED',NOW());
    """, (payment_id, booking_id, txn_ref, booking_amount))
    db_connection.commit()

    logging.info(f"Payment created: {txn_ref}, Booking: {booking_id}, Amount: {booking_amount}")

    # Step 3: Verify INITIATED
    cur.execute("SELECT payment_status FROM payments WHERE payment_id=%s;", (payment_id,))
    status = cur.fetchone()[0]
    assert status == "INITIATED"

    # Step 4: Transition to SUCCESS
    cur.execute("UPDATE payments SET payment_status='SUCCESS' WHERE payment_id=%s AND payment_status='INITIATED';", (payment_id,))
    db_connection.commit()
    assert cur.rowcount == 1
    cur.execute("SELECT payment_status FROM payments WHERE payment_id=%s;", (payment_id,))
    new_status = cur.fetchone()[0]
    assert new_status == "SUCCESS"

    # Step 5: Validate booking consistency
    cur.execute("""
        SELECT b.booking_status FROM bookings b
        JOIN payments p ON b.booking_id = p.booking_id
        WHERE p.payment_id=%s;
    """, (payment_id,))
    booking_status = cur.fetchone()[0]
    assert booking_status == "CONFIRMED"

    # Cleanup
    try:
        cur.execute("DELETE FROM payments WHERE payment_id=%s;", (payment_id,))
        db_connection.commit()
    finally:
        cur.close()

# --- Regression: failed payment scenario ---
@pytest.mark.regression
def test_failed_payment_does_not_confirm_booking(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT booking_id, total_amount FROM bookings WHERE booking_status='CONFIRMED' LIMIT 1;")
    booking = cur.fetchone()
    assert booking is not None
    booking_id, booking_amount = booking

    payment_id = int(time.time())
    txn_ref = f"TXN{payment_id}"
    cur.execute("""
        INSERT INTO payments (
            payment_id, booking_id, transaction_reference, amount,
            payment_method, payment_status, payment_date
        )
        VALUES (%s,%s,%s,%s,'UPI','INITIATED',NOW());
    """, (payment_id, booking_id, txn_ref, booking_amount))
    db_connection.commit()

    # Transition to FAILED
    cur.execute("UPDATE payments SET payment_status='FAILED' WHERE payment_id=%s AND payment_status='INITIATED';", (payment_id,))
    db_connection.commit()
    assert cur.rowcount == 1
    cur.execute("SELECT payment_status FROM payments WHERE payment_id=%s;", (payment_id,))
    status = cur.fetchone()[0]
    assert status == "FAILED"

    # Booking should remain CONFIRMED
    cur.execute("SELECT booking_status FROM bookings WHERE booking_id=%s;", (booking_id,))
    booking_status = cur.fetchone()[0]
    assert booking_status == "CONFIRMED"

    # Cleanup
    cur.execute("DELETE FROM payments WHERE payment_id=%s;", (payment_id,))
    db_connection.commit()
    cur.close()

# --- Regression: duplicate transaction reference ---
@pytest.mark.regression
def test_duplicate_transaction_reference(db_connection):
    cur = db_connection.cursor()
    txn_ref = "DUPLICATE123"
    payment_id1 = int(time.time())
    try:
        cur.execute("""
            INSERT INTO payments (
                payment_id, booking_id, transaction_reference, amount,
                payment_method, payment_status, payment_date
            )
            VALUES (%s,1,%s,1000,'CARD','INITIATED',NOW());
        """, (payment_id1, txn_ref))
        db_connection.commit()
        payment_id2 = payment_id1 + 1
        with pytest.raises(IntegrityError):
            cur.execute("""
                INSERT INTO payments (
                    payment_id, booking_id, transaction_reference, amount,
                    payment_method, payment_status, payment_date
                )
                VALUES (%s,1,%s,1000,'CARD','INITIATED',NOW());
            """, (payment_id2, txn_ref))
            db_connection.commit()
    finally:
        cur.execute("DELETE FROM payments WHERE transaction_reference=%s;", (txn_ref,))
        db_connection.commit()
    cur.close()

# --- Regression: invalid booking FK ---
@pytest.mark.regression
def test_invalid_booking_fk(db_connection):
    cur = db_connection.cursor()
    payment_id = int(time.time())
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO payments (
                payment_id, booking_id, transaction_reference, amount,
                payment_method, payment_status, payment_date
            )
            VALUES (%s,999999,'BADFK',1000,'CARD','INITIATED',NOW());
        """, (payment_id,))
        db_connection.commit()
    cur.close()

# --- Parameterized tests ---
@pytest.mark.parametrize("payment_method", ["CARD","UPI","NET_BANKING","WALLET"])
@pytest.mark.smoke
def test_valid_payment_methods_param(db_connection, payment_method):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM payments WHERE payment_method=%s;", (payment_method,))
    count = cur.fetchone()[0]
    assert count >= 0
    cur.close()

@pytest.mark.parametrize("status", ["INITIATED","SUCCESS","FAILED"])
@pytest.mark.smoke
def test_valid_payment_statuses_param(db_connection, status):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM payments WHERE payment_status=%s;", (status,))
    count = cur.fetchone()[0]
    # We don’t hard‑code expected counts; just assert the query runs and returns a non‑negative integer
    assert count >= 0
    cur.close()