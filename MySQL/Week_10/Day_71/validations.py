from mysql.connector import connect

conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb")

cur = conn.cursor()

expected_id = 4
expected_title = "Echoes of Eternity"
expected_author = "Meera Sharma"
expected_price = 700

# Fetching the record
cur.execute("SELECT * FROM books WHERE book_id = %s", (expected_id, ))
row = cur.fetchone()

# Unpacking the row
book_id, book_title, author, price = row

### -- VALIDATIONS --
# Verify book exists
assert row is not None, "Book does not record"

# Verify book title
assert book_title == expected_title, f"Name mismatched!{expected_title} != {book_title}"

# Verify book author
assert author == expected_author, f"Name mismatched!{expected_author} != {author}"

# Verify book price
assert price == expected_price, f"Price mismatched!{expected_price} != {price}"

print("All validations passed successfully!")

cur.close()
conn.close()