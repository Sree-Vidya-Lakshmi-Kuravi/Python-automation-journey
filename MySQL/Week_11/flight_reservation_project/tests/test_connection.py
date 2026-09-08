import pytest
import logging

def test_connection(db_connection):
    assert db_connection.is_connected(), "Connection to database failed"

def test_db_exists(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT DATABASE();")
    res = cur.fetchone()[0]
    assert res == "flight_reservation", f"Expected 'flight_reservation', got {res}"
    cur.close()

def test_tables_exists(db_connection):
    expected_tables = {'airlines', 'airports', 'aircrafts', 'customers', 'flights', 'flight_seats', 'bookings', 'passengers', 'payments', 'refunds'}
    cur = db_connection.cursor()
    cur.execute("SHOW TABLES;")
    res = {row[0] for row in cur.fetchall()}
    missing_tables = expected_tables - res
    assert not missing_tables, f"Missing tables: {missing_tables}"
    cur.close()

def test_cust_data_exists(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM customers;")
    count = cur.fetchone()[0]
    assert count >= 10, f"Customer count doesnot match.. Current customer count: {count}"
    cur.close()

def test_flight_data_exists(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM flights;")
    count = cur.fetchone()[0]
    assert count >= 10, f"Flight count doesnot match.. Current flight count: {count}"
    cur.close()