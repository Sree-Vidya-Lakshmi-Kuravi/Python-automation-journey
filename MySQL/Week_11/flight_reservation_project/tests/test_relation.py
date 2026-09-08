import pytest
from utils.db_assertions import *
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils()
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

def test_flight_airline(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.flight_number, a.airline_name FROM flights f 
        JOIN 
        airlines a 
        ON f.airline_id= a.airline_id;
        """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

def test_flight_airports(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.flight_number
        FROM flights f
        LEFT JOIN airports o ON f.origin_airport_id = o.airport_id
        LEFT JOIN airports d ON f.destination_airport_id = d.airport_id
        WHERE o.airport_id IS NULL OR d.airport_id IS NULL;
        """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

def test_booking_customer_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.booking_id
        FROM bookings b
        LEFT JOIN customers c ON b.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

def test_booking_flight_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT b.booking_id
        FROM bookings b
        LEFT JOIN flights f ON b.flight_id = f.flight_id
        WHERE f.flight_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

def test_payment_booking_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT p.payment_id
        FROM payments p
        LEFT JOIN bookings b ON p.booking_id = b.booking_id
        WHERE b.booking_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()