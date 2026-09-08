import pytest
import logging
import mysql.connector
from mysql.connector import Error

@pytest.fixture
def db_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "flight_reservation")
        yield conn
    except Error as e:
        pytest.fail("Database connection failed..")
    finally:
        if conn and conn.is_connected():
            conn.close()
