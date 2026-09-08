import pytest
from mysql.connector import connect
from mysql.connector import IntegrityError
from utils.db_assertions import *
from utils.db_utils import *

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri") 
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Airline count
def test_airline_count(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM airlines;")
    count = cur.fetchone()[0]
    assert_record_count(count, 3)
    cur.close()

# Airline codes are unique
def test_airline_code(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT airline_code, COUNT(*) FROM airlines GROUP BY airline_code HAVING COUNT(*) > 1;")
    duplicates = cur.fetchall()
    assert_record_count(len(duplicates), 0)

# Airline names are not NULL
def test_airline_names(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM airlines WHERE airline_name IS NULL;")
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)

# Duplicate airline code (expect IntegrityError)
def test_airline_duplicate_code(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO airlines (airline_code, airline_name) VALUES ('AI', 'Duplicate Air India');")
        db_connection.commit()
    cur.close()
    
# Retrieve airline by code (parameterized)
@pytest.mark.parametrize("code,expected_name", [
    ("AI", "Air India"),
    ("6E", "IndiGo"),
    ("SG", "SpiceJet"),
])
def test_retrieve_airline_by_code(db_connection, code, expected_name):
    cur = db_connection.cursor()
    cur.execute("SELECT airline_name FROM airlines WHERE airline_code = %s;", (code,))
    res = cur.fetchone()
    assert res is not None, f"No airline found for code {code}"
    assert res[0] == expected_name
    cur.close()