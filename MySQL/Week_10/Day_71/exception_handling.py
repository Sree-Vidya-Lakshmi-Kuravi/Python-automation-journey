from mysql.connector import connect
from mysql.connector import Error

try:
    conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb")
    if conn.is_connected():
        print("Connection established successfully..")
        cur = conn.cursor()

        cur.execute("SELECT * FROM books;")
        books = cur.fetchall()
        for b in books:
            print(b)

except Error as e:
    print("Error connecting to mysql server: ", e)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("Connection closed.")