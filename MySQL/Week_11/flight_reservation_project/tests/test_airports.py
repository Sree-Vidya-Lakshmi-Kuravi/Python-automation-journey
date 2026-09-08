import pytest
from mysql.connector import IntegrityError
from utils.db_assertions import assert_record_count
from utils.db_utils import DBUtils

@pytest.fixture(scope="module")
def db_connection():
    db = DBUtils(password="siri")  
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

# Test 1 — Airport count
def test_airport_count(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM airports;")
    count = cur.fetchone()[0]
    assert_record_count(count, 6)
    cur.close()

# Test 2 — Airport codes are unique
def test_airport_codes_unique(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT airport_code, COUNT(*)
        FROM airports
        GROUP BY airport_code
        HAVING COUNT(*) > 1;
    """)
    duplicates = cur.fetchall()
    assert_record_count(len(duplicates), 0)
    cur.close()

# Test 3 — Airport codes are valid
def test_expected_airport_codes_exist(db_connection):
    expected_codes = {"HYD", "BLR", "DEL", "BOM", "MAA", "CCU"}
    cur = db_connection.cursor()
    cur.execute("SELECT airport_code FROM airports;")
    codes = {row[0] for row in cur.fetchall()}
    missing = expected_codes - codes
    assert not missing, f"Missing airport codes: {missing}"
    cur.close()

# Test 4 — Required airport fields not NULL
def test_required_airport_fields(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT *
        FROM airports
        WHERE airport_code IS NULL
           OR airport_name IS NULL
           OR city IS NULL
           OR country IS NULL;
    """)
    missing = cur.fetchall()
    assert_record_count(len(missing), 0)
    cur.close()

# Test 5 — Duplicate airport code (expect IntegrityError)
def test_duplicate_airport_code(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("INSERT INTO airports (airport_code, airport_name, city, country) VALUES ('HYD', 'Duplicate Hyderabad', 'Hyderabad', 'India');")
        db_connection.commit()
    cur.close()

# Test 6 — Airport lookup (parameterized)
@pytest.mark.parametrize("code,expected_city", [
    ("HYD", "Hyderabad"),
    ("DEL", "Delhi"),
    ("BLR", "Bengaluru"),
])
def test_airport_lookup(db_connection, code, expected_city):
    cur = db_connection.cursor()
    cur.execute("SELECT city FROM airports WHERE airport_code = %s;", (code,))
    res = cur.fetchone()
    assert res is not None, f"No airport found for code {code}"
    assert res[0] == expected_city
    cur.close()