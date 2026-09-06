import mysql.connector
from mysql.connector import Error 

class DBUtils:
    def __init__(self, host = "localhost", user = "root", password = "", database = "mydb"):
        self.conn = None
        self.cur = None

        try:
            self.conn = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )

            self.cur = self.conn.cursor()
            print("Connection has been established successfully..")
        except Error as e:
            print("Error connected to database: ", e)


    def create_connection(self):
        return self.conn

    def execute_query(self, query, params = None):
        try:
            self.cur.execute(query, params)
        except Error as e:
            print("Unable to execute the query due to: ", e)

    def fetch_one(self, query, params = None):
        self.execute_query(query, params)
        return self.cur.fetchone()

    def fetch_all(self, query, params = None):
        self.execute_query(query, params)
        return self.cur.fetchall()

    def commit(self):
        try:
            self.conn.commit()
        except Error as e:
            print("Commiting the query failed due to: ", e)

    def rollback(self):
        try:
            self.conn.rollback()
        except Error as e:
            print("Rollbacking the query failed due to: ", e)

    def close_connection(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Database connection has been closed successfully..")


## Object creation
db = DBUtils(host = "localhost", user = "root", password = "siri", database = "mydb")
db.create_connection()

res = db.fetch_one("SELECT * FROM books WHERE book_id = %s", (2, ))
print("Fetch one record result: ", res)

f_res = db.fetch_all("SELECT * FROM books WHERE author LIKE %s", ('A%', ))
print("Fetch all record result: ", f_res)

db.execute_query("UPDATE books SET price = price + 100 WHERE book_id = %s", (3, ))
db.commit()

db.execute_query("DELETE FROM books WHERE book_id = %s", (6, ))
db.rollback()

db.close_connection()