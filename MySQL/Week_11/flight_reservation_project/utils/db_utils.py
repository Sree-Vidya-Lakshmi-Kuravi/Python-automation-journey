import logging
import mysql.connector
from mysql.connector import Error
import os

# Ensure the logs directory exists
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
    def __init__(self, host = "localhost", user = "root", password = "", database = "flight_reservation"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        logger.info("Host, User, Password and Database has been initialized..")

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database)
            logger.info("Connection established successfully..")
            return conn
        except Error as e:
            logger.error(f"Error connecting to database..{e}")
            return None

    def execute_query(self, query, params = None):
        conn = self.connect()
        if conn is None:
            return None
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            result = cur.fetchall()
            logger.info("Query executed successfully..")
            return result
        except Error as e:
            logger.error(f"Failed to execute the query..{e}")
            return None
        finally:
            cur.close()
            logger.info("Cursor closed successfully..")
            conn.close()
            logger.info("Connection closed successfully..")

    def execute_update(self, query, params = None):
        conn = self.connect()
        if conn is None:
            return 0
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            conn.commit()
            logger.info("Query updated successfully..")
            return cur.rowcount
        except Error as e:
            logger.error(f"Failed to update the query..{e}")
            return None
        finally:
            cur.close()
            logger.info("Cursor closed successfully..")
            conn.close()
            logger.info("Connection closed successfully..")

db = DBUtils()
connection = db.connect()
exe_query = db.execute_query("SELECT * FROM airlines")
print(exe_query)
upd_query = db.execute_update("UPDATE airlines SET airline_code = %s WHERE airline_id = %s;", ('DAL', 1))
print(upd_query)
print(db.execute_query("SELECT * FROM airlines"))