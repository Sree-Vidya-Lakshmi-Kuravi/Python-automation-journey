import pytest
from utils.db_assertions import assert_record_count
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri")  
    conn = db.connect()
    assert conn is not None, "Database connection failed"
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Important JOIN validation
@pytest.mark.regression
def test_flight_join_validation(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT f.flight_number, a.airline_name, ac.model,
               origin.airport_code AS origin,
               destination.airport_code AS destination,
               f.departure_time, f.arrival_time, f.base_fare, f.status
        FROM flights f
        JOIN airlines a ON f.airline_id = a.airline_id
        JOIN aircrafts ac ON f.aircraft_id = ac.aircraft_id
        JOIN airports origin ON f.origin_airport_id = origin.airport_id
        JOIN airports destination ON f.destination_airport_id = destination.airport_id;
    """)
    rows = cur.fetchall()
    # Verify every flight has all relationships
    assert_record_count(len(rows), 1)  # at least one valid flight
    cur.close()
