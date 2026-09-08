import pytest
from mysql.connector import IntegrityError
from utils.db_assertions import assert_record_count
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri")
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()


# Duplicate airline code
@pytest.mark.regression
def test_duplicate_airline_code(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO airlines (airline_code, airline_name) VALUES ('AI','Duplicate Air India');")
        db_connection.commit()
    cur.close()

# Duplicate airport code
@pytest.mark.regression
def test_duplicate_airport_code(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO airports (airport_code, airport_name, city, country) VALUES ('HYD','Duplicate Hyderabad','Hyderabad','India');")
        db_connection.commit()
    cur.close()

# Invalid airline_id in aircraft
@pytest.mark.regression
def test_invalid_airline_in_aircraft(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO aircrafts (aircraft_model, total_seats, airline_id) VALUES ('TestModel',150,99999);")
        db_connection.commit()
    cur.close()

# Invalid airport_id in flight
@pytest.mark.regression
def test_invalid_airport_in_flight(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO flights (flight_number, airline_id, aircraft_id, origin_airport_id, destination_airport_id, departure_time, arrival_time, base_fare, status)
            VALUES ('TST001',1,1,99999,99998,NOW(),NOW(),5000,'SCHEDULED');
        """)
        db_connection.commit()
    cur.close()

# Negative flight fare
@pytest.mark.regression
def test_negative_flight_fare(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO flights (flight_number, airline_id, aircraft_id, origin_airport_id, destination_airport_id, departure_time, arrival_time, base_fare, status)
            VALUES ('TST002',1,1,1,2,NOW(),NOW(),-1000,'SCHEDULED');
        """)
        db_connection.commit()
    cur.close()

# NULL aircraft model
@pytest.mark.regression
def test_null_aircraft_model(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO aircrafts (aircraft_model, total_seats, airline_id) VALUES (NULL,100,1);")
        db_connection.commit()
    cur.close()

@pytest.mark.parametrize("airport_code, expected_city", [
    ("HYD","Hyderabad"),
    ("DEL","New Delhi"),   # ✅ matches seed.sql
    ("BLR","Bengaluru"),
    ("MAA","Chennai"),
])
def test_airport_city(db_connection, airport_code, expected_city):
    cur = db_connection.cursor()
    cur.execute("SELECT city FROM airports WHERE airport_code=%s;", (airport_code,))
    res = cur.fetchone()
    assert res is not None
    assert res[0] == expected_city
    cur.close()

@pytest.mark.parametrize("code, expected_name", [
    ("AI","Air India"),
    ("6E","IndiGo"),
    ("SG","SpiceJet"),
])
def test_retrieve_airline_by_code(db_connection, code, expected_name):
    cur = db_connection.cursor()
    cur.execute("SELECT airline_name FROM airlines WHERE airline_code=%s;", (code,))
    res = cur.fetchone()
    assert res is not None
    assert res[0] == expected_name
    cur.close()