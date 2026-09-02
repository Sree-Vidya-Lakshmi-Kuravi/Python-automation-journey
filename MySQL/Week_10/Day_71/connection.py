from mysql.connector import connect

print("Creating connection..")
conn = connect(host = 'localhost',
               user = 'root',
               password = 'siri')

cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS mydb;")
print("Database created successfully..")

cur.execute("SHOW DATABASES;")
print(cur.fetchall())

cur.execute("USE mydb;")
print("Database used successfully..")

cur.execute("""CREATE TABLE IF NOT EXISTS books(
            book_id INT PRIMARY KEY,
            book_title VARCHAR(50),
            author VARCHAR(50),
            price DECIMAL(10, 2));""")
print("Table created successfully..")

new_books = [
    (1, 'The Silent River', 'Arundhati Rao', 450),
    (2, 'Whispers of the Wind', 'Kiran Desai', 520),
    (3, 'Shadows of Time', 'Ravi Menon', 600),
    (4, 'Echoes of Eternity', 'Meera Sharma', 700),
    (5, 'Journey to Dawn', 'Anil Kapoor', 550)]
cur.executemany("""
    INSERT INTO books(book_id, book_title, author, price) VALUES (%s, %s, %s, %s)""", new_books)
print("New books added successfully..")

cur.execute("SELECT * FROM books;")
book_list = cur.fetchall()
for b in book_list:
    print(b)
print("Data displayed successfully..")

cur.close()
conn.commit()
conn.close()
print("Connected closed successfully..")