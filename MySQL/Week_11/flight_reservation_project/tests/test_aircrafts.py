import pytest
from mysql.connector import IntegrityError
from utils.db_assertions import assert_record_count
from utils.db_utils import DBUtils

@pytest.fixture(scope="module")
def db_connection():
    db = DBUtils(password="siri")  
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Test 1 — Aircraft count
def test_aircraft_count(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM aircrafts;")
    count = cur.fetchone()[0]
    assert_record_count(count, 5)
    cur.close()

# Test 2 — Every aircraft belongs to an airline
def test_aircraft_airline_relationship(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT a.* FROM aircrafts a
        LEFT JOIN airlines al 
        ON a.airline_id = al.airline_id
        WHERE al.airline_id IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Test 3 — Aircraft seats are positive
def test_aircraft_seats_positive(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM aircrafts WHERE total_seats <= 0;")
    invalid = cur.fetchall()
    assert_record_count(len(invalid), 0)
    cur.close()

# Test 4 — Invalid airline FK (expect IntegrityError)
def test_invalid_airline_fk(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO aircrafts (model, total_seats, airline_id)
            VALUES ('TestModel', 150, 99999);
        """)
        db_connection.commit()
    cur.close()

# Test 5 — Aircraft model cannot be NULL (expect IntegrityError)
def test_aircraft_model_not_null(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO aircrafts (model, total_seats, airline_id, aircraft_id)
            VALUES (NULL, 100, 1, 1);
        """)
        db_connection.commit()
    cur.close()