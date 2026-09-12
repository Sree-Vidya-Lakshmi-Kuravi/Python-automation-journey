import logging
import mysql.connector
from mysql.connector import Error
import os
from config.db_config import DB_CONFIG

os.makedirs("Week_11/flight_reservation_project/logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("Week_11/flight_reservation_project/logs/test_execution.log")
    ]
)

logger = logging.getLogger(__name__)

class DBUtils:
    def __init__(self):
        self.config = DB_CONFIG
        logger.info("Database configuration loaded from environment variables.")

    def connect(self):
        try:
            conn = mysql.connector.connect(**self.config)
            logger.info("Connection established successfully.")
            return conn
        except Error as e:
            logger.error(f"Error connecting to database: {e}")
            return None

    def execute_query(self, query, params=None):
        conn = self.connect()
        if conn is None:
            return None
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            result = cur.fetchall()
            logger.info("Query executed successfully.")
            return result
        except Error as e:
            logger.error(f"Failed to execute query: {e}")
            return None
        finally:
            cur.close()
            conn.close()

    def execute_update(self, query, params=None):
        conn = self.connect()
        if conn is None:
            return 0
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            conn.commit()
            logger.info("Update executed successfully.")
            return cur.rowcount
        except Error as e:
            logger.error(f"Failed to execute update: {e}")
            return None
        finally:
            cur.close()
            conn.close()
