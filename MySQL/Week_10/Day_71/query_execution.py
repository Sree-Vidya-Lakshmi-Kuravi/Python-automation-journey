from mysql.connector import connect

conn = connect(
        host = "localhost",
        user = "root",
        password = "siri",
        database = "mydb"
)

cur = conn.cursor()

query_1 = cur.execute("Select * from books;")
q1_res = cur.fetchall()

query_2 = cur.execute("Select * from books where price > %s;", ((500,)))
q2_res = cur.fetchall()

query_3 = cur.execute("Select * from books where price < %s;", ((500,)))
q3_res = cur.fetchall()

query_4 = cur.execute("Select * from books where price > %s;", ((400,)))
q4_res = cur.fetchall()

query_5 = cur.execute("Select * from books order by price desc;")
q5_res = cur.fetchall()


print("Query 1 result: ", q1_res)
print("Query 2 result: ", q2_res)
print("Query 3 result: ", q3_res)
print("Query 4 result: ", q4_res)
print("Query 5 result: ", q5_res)

cur.close()
conn.close()

# cur = conn.cursor()

# cur.execute("SELECT * FROM books;")
# book_list = cur.fetchall()
# for b in book_list:
#     print(b)

# cur.execute("SELECT AVG(price) FROM books;")
# avg_price = cur.fetchall()
# print(avg_price)

# cur.execute("SELECT * FROM books WHERE price >= 200.00;")
# prices = cur.fetchall()
# for p in prices:
#     print(p)

# cur.execute("SELECT * FROM books ORDER BY price DESC;")
# price_order = cur.fetchall()
# for p in price_order:
#     print(p)