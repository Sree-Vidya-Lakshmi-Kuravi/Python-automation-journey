import pytest
from mysql.connector import IntegrityError
from utils.db_utils import DBUtils

@pytest.fixture
def db_connection():
    db = DBUtils(password = "siri")
    conn = db.connect()
    yield conn
    if conn and conn.is_connected():
        conn.close()

# table accessible
@pytest.mark.smoke
def test_seat_table_accessible(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM flight_seats;")
    count = cur.fetchone()[0]
    assert count >= 0
    cur.close()

# unavailable seat cannot be reserved
def test_unavailable_seat_reservation(db_connection):
    cur = db_connection.cursor()
    # Pick a HELD seat
    cur.execute("SELECT seat_id FROM flight_seats WHERE seat_status='HELD' LIMIT 1;")
    seat = cur.fetchone()
    assert seat is not None, "No HELD seat found"
    seat_id = seat[0]

    # Try to reserve again
    cur.execute("""
        UPDATE flight_seats SET seat_status='HELD'
        WHERE seat_id=%s AND seat_status='AVAILABLE';
    """, (seat_id,))
    db_connection.commit()
    affected_rows = cur.rowcount
    assert affected_rows == 0, f"Expected 0 rows updated, got {affected_rows}"
    cur.close()

# BOOKED seat protection
@pytest.mark.regression
def test_booked_seat_protection(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT seat_id FROM flight_seats WHERE seat_status='BOOKED' LIMIT 1;")
    seat = cur.fetchone()
    assert seat is not None, "No BOOKED seat found"
    seat_id = seat[0]

    cur.execute("""
        UPDATE flight_seats SET seat_status='HELD'
        WHERE seat_id=%s AND seat_status='AVAILABLE';
    """, (seat_id,))
    db_connection.commit()
    affected_rows = cur.rowcount
    assert affected_rows == 0

    # Verify still BOOKED
    cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
    status = cur.fetchone()[0]
    assert status == "BOOKED"
    cur.close()

# seat release HELD → AVAILABLE
@pytest.mark.sanity
def test_seat_release(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT seat_id FROM flight_seats WHERE seat_status='HELD' LIMIT 1;")
    seat = cur.fetchone()
    assert seat is not None, "No HELD seat found"
    seat_id = seat[0]

    try:
        cur.execute("""
            UPDATE flight_seats SET seat_status='AVAILABLE'
            WHERE seat_id=%s AND seat_status='HELD';
        """, (seat_id,))
        db_connection.commit()
        affected_rows = cur.rowcount
        assert affected_rows == 1

        cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
        status = cur.fetchone()[0]
        assert status == "AVAILABLE"
    finally:
        # Cleanup: restore HELD if needed
        cur.execute("UPDATE flight_seats SET seat_status='HELD' WHERE seat_id=%s;", (seat_id,))
        db_connection.commit()
    cur.close()

# Regression: BOOKED → AVAILABLE (document behavior)
@pytest.mark.regression
def test_booked_to_available(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT seat_id FROM flight_seats WHERE seat_status='BOOKED' LIMIT 1;")
    seat = cur.fetchone()
    assert seat is not None, "No BOOKED seat found"
    seat_id = seat[0]

    cur.execute("""
        UPDATE flight_seats SET seat_status='AVAILABLE'
        WHERE seat_id=%s AND seat_status='BOOKED';
    """, (seat_id,))
    db_connection.commit()
    affected_rows = cur.rowcount

    # Document current behavior
    if affected_rows == 0:
        print("BOOKED → AVAILABLE not permitted (expected).")
    else:
        print("BOOKED → AVAILABLE permitted (represents cancellation).")

    cur.close()

# Regression: composite uniqueness
@pytest.mark.regression
def test_duplicate_seat_insertion(db_connection):
    cur = db_connection.cursor()
    flight_id = 1
    seat_number = "99Z"
    try:
        cur.execute("""
            INSERT INTO flight_seats (flight_id, seat_number, seat_class, seat_status)
            VALUES (%s,%s,'ECONOMY','AVAILABLE');
        """, (flight_id, seat_number))
        db_connection.commit()
        with pytest.raises(IntegrityError):
            cur.execute("""
                INSERT INTO flight_seats (flight_id, seat_number, seat_class, seat_status)
                VALUES (%s,%s,'ECONOMY','AVAILABLE');
            """, (flight_id, seat_number))
            db_connection.commit()
    finally:
        cur.execute("DELETE FROM flight_seats WHERE flight_id=%s AND seat_number=%s;", (flight_id, seat_number))
        db_connection.commit()
    cur.close()

# Regression: invalid flight FK
@pytest.mark.regression
def test_invalid_flight_fk(db_connection):
    cur = db_connection.cursor()
    with pytest.raises(IntegrityError):
        cur.execute("""
            INSERT INTO flight_seats (flight_id, seat_number, seat_class, seat_status)
            VALUES (99999,'X1','ECONOMY','AVAILABLE');
        """)
        db_connection.commit()
    cur.close()

# Regression: seat distribution aggregation
@pytest.mark.regression
def test_seat_distribution_report(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        SELECT flight_id, seat_class, seat_status, COUNT(*) AS seat_count
        FROM flight_seats
        GROUP BY flight_id, seat_class, seat_status
        ORDER BY flight_id, seat_class, seat_status;
    """)
    results = cur.fetchall()
    assert len(results) > 0
    for row in results:
        flight_id, seat_class, seat_status, seat_count = row
        assert seat_count >= 0
    cur.close()

# Regression: transaction rollback
@pytest.mark.regression
def test_transaction_rollback(db_connection):
    flight_id = 1
    cur = db_connection.cursor()
    cur.execute("SELECT seat_id FROM flight_seats WHERE flight_id=%s AND seat_status='AVAILABLE' LIMIT 1;", (flight_id,))
    seat = cur.fetchone()
    assert seat is not None, "No AVAILABLE seat found"
    seat_id = seat[0]

    try:
        db_connection.start_transaction()
        cur.execute("UPDATE flight_seats SET seat_status='HELD' WHERE seat_id=%s;", (seat_id,))
        cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
        status = cur.fetchone()[0]
        assert status == "HELD"
        db_connection.rollback()
        cur.execute("SELECT seat_status FROM flight_seats WHERE seat_id=%s;", (seat_id,))
        status_after = cur.fetchone()[0]
        assert status_after == "AVAILABLE"
    finally:
        cur.close()