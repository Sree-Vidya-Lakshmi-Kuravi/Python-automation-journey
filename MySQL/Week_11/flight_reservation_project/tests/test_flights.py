import pytest
from utils.db_assertions import assert_record_count
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri")  # adjust credentials
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Test 1 — Flight count
def test_flight_count(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM flights;")
    count = cur.fetchone()[0]
    assert_record_count(count, 10)
    cur.close()

# Test 2 — Flight numbers are unique
def test_flight_numbers_unique(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT flight_number, COUNT(*)
        FROM flights
        GROUP BY flight_number
        HAVING COUNT(*) > 1;
    """)
    duplicates = cur.fetchall()
    assert_record_count(len(duplicates), 0)
    cur.close()

# Test 3 — Flight has valid airline
def test_flight_airline_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.*
        FROM flights f
        LEFT JOIN airlines a ON f.airline_id = a.airline_id
        WHERE a.airline_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Test 4 — Flight has valid aircraft
def test_flight_aircraft_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.*
        FROM flights f
        LEFT JOIN aircrafts ac ON f.aircraft_id = ac.aircraft_id
        WHERE ac.aircraft_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Test 5 — Flight has valid origin airport
def test_flight_origin_airport_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.*
        FROM flights f
        LEFT JOIN airports o ON f.origin_airport_id = o.airport_id
        WHERE o.airport_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Test 6 — Flight has valid destination airport
def test_flight_destination_airport_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.*
        FROM flights f
        LEFT JOIN airports d ON f.destination_airport_id = d.airport_id
        WHERE d.airport_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Rule 1 — Origin ≠ Destination
def test_origin_not_equal_destination(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM flights WHERE origin_airport_id = destination_airport_id;")
    invalid = cur.fetchall()
    assert_record_count(len(invalid), 0)
    cur.close()

# Rule 2 — Arrival after departure
def test_arrival_after_departure(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM flights WHERE arrival_time <= departure_time;")
    invalid = cur.fetchall()
    assert_record_count(len(invalid), 0)
    cur.close()

# Rule 3 — Fare must be positive
def test_fare_positive(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM flights WHERE base_fare <= 0;")
    invalid = cur.fetchall()
    assert_record_count(len(invalid), 0)
    cur.close()

# Rule 4 — Flight status must be valid
def test_flight_status_valid(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT *
        FROM flights
        WHERE status NOT IN ('SCHEDULED', 'BOARDING', 'COMPLETED', 'CANCELLED');
    """)
    invalid = cur.fetchall()
    assert_record_count(len(invalid), 0)
    cur.close()