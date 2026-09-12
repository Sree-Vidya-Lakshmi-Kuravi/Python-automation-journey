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

# --- Transaction basics ---
@pytest.mark.smoke
def test_transaction_rollback(db_connection):
    cur = db_connection.cursor()
    email = f"rollback{int(time.time())}@test.com"
    customer_id = int(time.time())
    cur.execute("START TRANSACTION;")
    cur.execute("""
        INSERT INTO customers (customer_id, first_name, last_name, email, phone, date_of_birth)
        VALUES (%s,'Test','Rollback',%s,'9999999999','2000-01-01');
    """, (customer_id, email))
    cur.execute("ROLLBACK;")
    cur.execute("SELECT * FROM customers WHERE email=%s;", (email,))
    assert cur.fetchone() is None
    cur.close()

@pytest.mark.smoke
def test_transaction_commit(db_connection):
    cur = db_connection.cursor()
    email = f"commit{int(time.time())}@test.com"
    customer_id = int(time.time())
    cur.execute("START TRANSACTION;")
    cur.execute("""
        INSERT INTO customers (customer_id, first_name, last_name, email, phone, date_of_birth)
        VALUES (%s,'Test','Commit',%s,'9999999999','2000-01-01');
    """, (customer_id, email))
    cur.execute("COMMIT;")
    cur.execute("SELECT * FROM customers WHERE email=%s;", (email,))
    row = cur.fetchone()
    assert row is not None
    # cleanup
    cur.execute("DELETE FROM customers WHERE email=%s;", (email,))
    db_connection.commit()
    cur.close()

@pytest.mark.regression
def test_transaction_savepoint(db_connection):
    cur = db_connection.cursor()
    email_a = f"a{int(time.time())}@test.com"
    email_b = f"b{int(time.time())}@test.com"
    id_a = int(time.time())
    id_b = id_a + 1
    cur.execute("START TRANSACTION;")
    cur.execute("""
        INSERT INTO customers (customer_id, first_name, last_name, email, phone)
        VALUES (%s,'A','Savepoint',%s,'9999999999');
    """, (id_a, email_a))
    cur.execute("SAVEPOINT customer_savepoint;")
    cur.execute("""
        INSERT INTO customers (customer_id, first_name, last_name, email, phone)
        VALUES (%s,'B','Savepoint',%s,'9999999999');
    """, (id_b, email_b))
    cur.execute("ROLLBACK TO SAVEPOINT customer_savepoint;")
    cur.execute("COMMIT;")
    cur.execute("SELECT * FROM customers WHERE email=%s;", (email_a,))
    assert cur.fetchone() is not None
    cur.execute("SELECT * FROM customers WHERE email=%s;", (email_b,))
    assert cur.fetchone() is None
    # cleanup
    cur.execute("DELETE FROM customers WHERE email=%s;", (email_a,))
    db_connection.commit()
    cur.close()

# --- End-to-end booking transaction ---
@pytest.mark.sanity
def test_complete_booking_transaction(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT customer_id FROM customers LIMIT 1;")
    row = cur.fetchone()
    assert row is not None, "No customer found"
    customer_id = row[0]

    cur.execute("SELECT flight_id FROM flights WHERE status='SCHEDULED' LIMIT 1;")
    row = cur.fetchone()
    assert row is not None, "No scheduled flight found"
    flight_id = row[0]

    cur.execute("SELECT seat_id FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE' LIMIT 1;", (flight_id,))
    row = cur.fetchone()
    assert row is not None, "No available seat found"
    seat_id = row[0]

    booking_id = int(time.time())
    passenger_id = booking_id + 1
    payment_id = booking_id + 2
    txn_ref = f"TXN{booking_id}"

    cur.execute("START TRANSACTION;")
    try:
        cur.execute("""
            INSERT INTO bookings (booking_id, booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount)
            VALUES (%s,%s,%s,%s,%s,NOW(),'PENDING',5000);
        """, (booking_id, f"TEST{booking_id}", customer_id, flight_id, seat_id))
        cur.execute("""
            INSERT INTO passengers (passenger_id, booking_id, first_name, last_name, passport_number, date_of_birth)
            VALUES (%s,%s,'Test','Passenger','P12345','2000-01-01');
        """, (passenger_id, booking_id))
        cur.execute("UPDATE flight_seats SET seat_status='BOOKED' WHERE seat_id=%s;", (seat_id,))
        cur.execute("""
            INSERT INTO payments (payment_id, booking_id, transaction_reference, amount, payment_method, payment_status, payment_date)
            VALUES (%s,%s,%s,5000,'CARD','SUCCESS',NOW());
        """, (payment_id, booking_id, txn_ref))
        cur.execute("COMMIT;")
    except Exception:
        cur.execute("ROLLBACK;")
        raise

    # verify
    cur.execute("SELECT booking_status FROM bookings WHERE booking_id=%s;", (booking_id,))
    assert cur.fetchone()[0] == "PENDING"
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    assert cur.fetchone()[0] == "BOOKED"
    cur.execute("SELECT payment_status FROM payments WHERE payment_id=%s;", (payment_id,))
    assert cur.fetchone()[0] == "SUCCESS"
    cur.execute("SELECT * FROM passengers WHERE booking_id=%s;", (booking_id,))
    assert cur.fetchone() is not None

    # cleanup
    cur.execute("DELETE FROM passengers WHERE booking_id=%s;", (booking_id,))
    cur.execute("DELETE FROM payments WHERE payment_id=%s;", (payment_id,))
    cur.execute("DELETE FROM bookings WHERE booking_id=%s;", (booking_id,))
    cur.execute("UPDATE flight_seats SET seat_status='AVAILABLE' WHERE seat_id=%s;", (seat_id,))
    db_connection.commit()
    cur.close()

# --- Rollback scenarios ---
@pytest.mark.regression
def test_full_booking_rollback(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT customer_id FROM customers LIMIT 1;")
    row = cur.fetchone()
    assert row is not None, "No customer found"
    customer_id = row[0]

    cur.execute("SELECT flight_id FROM flights WHERE status='SCHEDULED' LIMIT 1;")
    row = cur.fetchone()
    assert row is not None, "No scheduled flight found"
    flight_id = row[0]

    cur.execute("SELECT seat_id FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE' LIMIT 1;", (flight_id,))
    row = cur.fetchone()
    assert row is not None, "No available seat found"
    seat_id = row[0]

    booking_id = int(time.time())
    passenger_id = booking_id + 1
    payment_id = booking_id + 2

    cur.execute("START TRANSACTION;")
    try:
        cur.execute("""
            INSERT INTO bookings (booking_id, booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount)
            VALUES (%s,%s,%s,%s,%s,NOW(),'PENDING',5000);
        """, (booking_id, f"ROLL{booking_id}", customer_id, flight_id, seat_id))
        cur.execute("""
            INSERT INTO passengers (passenger_id, booking_id, first_name, last_name, passport_number, date_of_birth)
            VALUES (%s,%s,'Fail','Passenger','X12345','2000-01-01');
        """, (passenger_id, booking_id))
        cur.execute("UPDATE flight_seats SET seat_status='BOOKED' WHERE seat_id=%s;", (seat_id,))
        cur.execute("""
            INSERT INTO payments (payment_id, booking_id, transaction_reference, amount, payment_method, payment_status, payment_date)
            VALUES (%s,%s,'FAILTXN',5000,'CARD','SUCCESS',NOW());
        """, (payment_id, booking_id))
        raise Exception("Forced failure")
    except Exception:
        cur.execute("ROLLBACK;")

    # verify rollback
    cur.execute("SELECT * FROM bookings WHERE booking_id=%s;", (booking_id,))
    assert cur.fetchone() is None
    cur.execute("SELECT * FROM passengers WHERE booking_id=%s;", (booking_id,))
    assert cur.fetchone() is None
    cur.execute("SELECT * FROM payments WHERE payment_id=%s;", (payment_id,))
    assert cur.fetchone() is None
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    seat_status = cur.fetchone()[0]
    assert seat_status == "AVAILABLE"

    cur.close()