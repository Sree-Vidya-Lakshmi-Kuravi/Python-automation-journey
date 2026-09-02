from mysql.connector import connect

conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb"
)

# fetch all rows
cur = conn.cursor()
cur.execute("SELECT * FROM books;")
book_list = cur.fetchall()
for b in book_list:
    print(b)

# fetch 1 row
cur = conn.cursor()
cur.execute("SELECT * FROM books;")
book_list = cur.fetchone()
print(book_list)
cur.fetchall()  # discard remaining rows

# fetch 3 rows
cur = conn.cursor()
cur.execute("SELECT * FROM books;")
rows = cur.fetchmany(3)   
for row in rows:
    print(row)
cur.fetchall() # discard remaining rows

cur.close()
conn.close()