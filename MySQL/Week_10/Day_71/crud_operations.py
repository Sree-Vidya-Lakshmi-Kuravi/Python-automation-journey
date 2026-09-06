from mysql.connector import connect

conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb")

cur = conn.cursor()

create_books = [
    (6, 'Beyond the Horizon', 'Sanjay Patel', 480),
    (7, 'The Last Kingdom', 'Priya Nair', 650),
    (8, 'Dreams of Tomorrow', 'Vikram Joshi', 530)
]
cur.executemany(
    """INSERT INTO books (book_id, book_title, author, price)
       VALUES (%s, %s, %s, %s)""", create_books)
conn.commit()
print("Data added successfully..")

# --- READ (Select data) ---
cur.execute("SELECT * FROM books;")
read_books = cur.fetchall()
for b in read_books:
    print(b)

# --- UPDATE (Modify data) ---
cur.execute("""
    UPDATE books
    SET author = 'Kiran D'
    WHERE book_id = 2;
""")
conn.commit()
print("\nData updated successfully..")

cur.execute("SELECT * FROM books WHERE book_id = 2;")
up_books = cur.fetchall()
for b in up_books:
    print(b)

# --- DELETE (Remove data) ---
cur.execute("DELETE FROM books WHERE book_id = 5;")
conn.commit()
print("\nRow deleted successfully..")

cur.execute("SELECT * FROM books;")
delete_books = cur.fetchall()
for b in delete_books:
    print(b)

# --- ROLLBACK DEMO ---
# Here we delete a row but DO NOT commit yet
cur.execute("DELETE FROM books WHERE book_id = 6;")
print("\nDeleted book_id=6 (not committed yet)..")

# Rollback will undo the delete
conn.rollback()
print("Rollback performed..")

cur.execute("SELECT * FROM books;")
rollback_books = cur.fetchall()
print("Books after rollback:")
for b in rollback_books:
    print(b)

# Close resources
cur.close()
conn.close()

