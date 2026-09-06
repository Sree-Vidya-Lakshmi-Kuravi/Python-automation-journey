from mysql.connector import connect

conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb")

cur = conn.cursor()

## -- PARAMETRIZED QUERIES -- 

book_id = 3
new_book_query = """
    SELECT * FROM books WHERE 
    book_id = %s""" 
cur.execute(new_book_query, (book_id, ))
ns = cur.fetchall()
for n in ns:
    print(n)


new_books_query = """
    SELECT * FROM books WHERE 
    author LIKE %s
    OR
    book_title LIKE %s""" 
cur.execute(new_books_query, ('A%', '%n%'))
rows = cur.fetchall()
for r in rows:
    print(r)
