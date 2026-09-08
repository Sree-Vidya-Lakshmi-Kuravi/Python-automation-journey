import pytest
from mysql.connector import IntegrityError
from utils.db_assertions import assert_field_count
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils(password="siri")
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

@pytest.mark.sanity
def test_airport_crud(db_connection):
    cur = db_connection.cursor()

    # CREATE
    cur.execute("INSERT INTO airports (airport_id, airport_code, airport_name, city, country) VALUES (9999, 'TST', 'Test Airport', 'TestCity', 'TestLand');")
    db_connection.commit()

    # READ
    cur.execute("SELECT city FROM airports WHERE airport_code='TST';")
    res = cur.fetchone()
    assert_field_count(res[0], "TestCity")

    # UPDATE
    cur.execute("UPDATE airports SET city='UpdatedCity' WHERE airport_code='TST';")
    db_connection.commit()

    # READ again
    cur.execute("SELECT city FROM airports WHERE airport_code='TST';")
    res = cur.fetchone()
    assert_field_count(res[0], "UpdatedCity")

    # DELETE
    cur.execute("DELETE FROM airports WHERE airport_code='TST';")
    db_connection.commit()

    # Final READ
    cur.execute("SELECT * FROM airports WHERE airport_code='TST';")
    res = cur.fetchall()
    assert len(res) == 0

    cur.close()