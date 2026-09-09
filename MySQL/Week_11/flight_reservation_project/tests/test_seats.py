import pytest
from mysql.connector import connect
from mysql.connector import IntegrityError
from utils.db_utils import DBUtils
from utils.db_assertions import *

@pytest.fixture
def db_connection():
    db = DBUtils(password = "siri")
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Validate seat data
@pytest.mark.smoke
def test_seat_exists(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM flight_seats;")
    count = cur.fetchone()[0]
    assert_record_count(count, 1)
    cur.close()

@pytest.mark.regression
def test_seat_flight(db_connection):
    cur = db_connection.cursor()
    cur.execute("""SELECT fs.* FROM flight_seats fs
LEFT JOIN flights f ON fs.flight_id= f.flight_id
WHERE f.flight_id IS NULL;""")
    invalid = cur.fetchall()
    assert_no_duplicate(invalid)
    cur.close()

@pytest.mark.regression
def test_no_duplicate_seat(db_connection):
    cur = db_connection.cursor()
    cur.execute("""SELECT flight_id, seat_number, COUNT(*) FROM flight_seats
GROUP BY flight_id, seat_number HAVING COUNT(*)>1;""")
    duplicates = cur.fetchall()
    assert_no_duplicate(duplicates)
    cur.close()

# Validate seat classes
@pytest.mark.regression
def test_seat_class(db_connection):
    cur = db_connection.cursor()
    cur.execute("""SELECT * FROM flight_seats WHERE seat_class NOT IN
('ECONOMY','PREMIUM_ECONOMY','BUSINESS');""")
    seats = cur.fetchall()
    assert_no_duplicate(seats)
    cur.close()

# Validate seat statuses
@pytest.mark.regression
def test_seat_status(db_connection):
    cur = db_connection.cursor()
    cur.execute("""SELECT * FROM flight_seats WHERE seat_status NOT IN
('AVAILABLE','HELD','BOOKED');""")
    seat_status = cur.fetchall()
    assert_no_duplicate(seat_status)
    cur.close()

# Count available seats
@pytest.mark.regression
def test_count_avail_seats(db_connection):
    flight_id = 1
    expected_count = 2
    cur = db_connection.cursor()
    cur.execute("""SELECT COUNT(*) FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE';""", (flight_id, ))
    count = cur.fetchone()[0]
    assert count == expected_count, f"Expected {expected_count}, got {count}"
    cur.close()

# Retrieve available seats
@pytest.mark.regression
def test_retrieve_avail_seats(db_connection):
    flight_id = 1
    cur = db_connection.cursor()
    cur.execute("""SELECT seat_number, seat_class FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE';""", (flight_id, ))
    results = cur.fetchall()
    assert len(results) > 0, "No available seats found"
    for seat_number, seat_class in results:
        assert isinstance(seat_number, str) or isinstance(seat_number, int)
        assert seat_class in ("ECONOMY","PREMIUM_ECONOMY","BUSINESS")
    cur.close()

# Parameterized seat-class validation
@pytest.mark.parametrize("seat_class", ["ECONOMY","PREMIUM_ECONOMY","BUSINESS"])
@pytest.mark.smoke
def test_valid_seat_classes_param(db_connection, seat_class):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM flight_seats WHERE seat_class=%s;", (seat_class,))
    count = cur.fetchone()[0]
    assert_record_count(count, 1)  
    cur.close()

# Implement seat reservation
def test_seat_reservation(db_connection):
    flight_id = 1  # adjust to a valid flight_id
    cur = db_connection.cursor()

    # Step 1: Retrieve one available seat
    cur.execute("""
        SELECT seat_id, seat_number
        FROM flight_seats
        WHERE flight_id=%s AND seat_status='AVAILABLE'
        LIMIT 1;
    """, (flight_id,))
    seat = cur.fetchone()
    assert seat is not None, f"No available seat found for flight {flight_id}"
    seat_id, seat_number = seat

    # Step 2: Update seat status to HELD
    cur.execute("""
        UPDATE flight_seats
        SET seat_status='HELD'
        WHERE seat_id=%s AND seat_status='AVAILABLE';
    """, (seat_id,))
    db_connection.commit()

    # Step 3: Verify affected row count
    affected_rows = cur.rowcount
    assert affected_rows == 1, f"Expected 1 row updated, got {affected_rows}"

    # Step 4: Query again to verify status
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    status = cur.fetchone()[0]
    assert status == "HELD", f"Expected HELD, got {status}"

    cur.close()

