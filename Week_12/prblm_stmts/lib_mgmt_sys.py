# === LIBRARY MANAGEMENT SYSTEM ===
books = []

num_of_books = int(input("Enter the number of books the library wants to register:"))

if num_of_books <= 0:
    print("Invalid number of books")
    exit()

for b in range(num_of_books):
    book_id = input("Book ID:")
    book_title = input("Book Title:")
    author = input("Author:")
    genre = input("Genre:")
    num_of_copies = int(input("Number of Copies:"))

    book_data = {
        'id': book_id,
        'title': book_title,
        'author': author,
        'genre': genre,
        'copies': num_of_copies
    }
    books.append(book_data)  # list of dictionaries


def display_books():
    print("========== LIBRARY BOOKS ==========")
    for book in books:
        print("ID:", book['id'])
        print("Title:", book['title'])
        print("Author:", book['author'])
        print("Genre:", book['genre'])
        print("Copies:", book['copies'])

        if book['copies'] > 0:
            status = "Available"
        else:
            status = "Not Available"

        print("Status:", status)
        print("-" * 15)

# display_books()

total_num_of_copies = num_of_avail_books = num_of_unavail_books = 0
total_books = len(books)

def lib_stats():
    for book in books:
        total_num_of_copies += book['copies']
        if book['copies'] > 0:
            num_of_avail_books += 1
        else:
            num_of_unavail_books += 1

    print("===== LIBRARY STATISTICS =====")
    print("Total Books:", total_books)
    print("Total Copies:", total_num_of_copies)
    print("Available Books:", num_of_avail_books)
    print("Unavailable Books:", num_of_unavail_books)

# Highest num of copies
high_num_of_copies = books[0]
for b in books:
    if b['copies'] > high_num_of_copies['copies']:
        high_num_of_copies = b

print("---- BOOK WITH HIGHEST COPIES ----")
print("Title:", high_num_of_copies['title'])
print("Author:", high_num_of_copies['author'])
print("Copies:", high_num_of_copies['copies'])

# Lowest num of copies
low_num_of_copies = books[0]
for b in books:
    if b['copies'] < low_num_of_copies['copies']:
        low_num_of_copies = b

print("---- BOOK WITH LOWEST COPIES ----")
print("Title:", low_num_of_copies['title'])
print("Author:", low_num_of_copies['author'])
print("Copies:", low_num_of_copies['copies'])

# Search book by ID
search_id = input("Enter Book ID to search:")
found = False

for b in books:
    if b['id'] == search_id:
        print("----- BOOK FOUND -----")
        print("ID:", b['id'])
        print("Title:", b['title'])
        print("Author:", b['author'])
        print("Genre:", b['genre'])
        print("Copies:", b['copies'])

        if b['copies'] > 0:
            print("Status: Available")
        else:
            print("Status: Unavailable")

        found = True
        break

if not found:
    print(f"Book with ID: {search_id} not found")

# Search Books by Genre

search_genre = input("\nEnter genre to search: ")
found = False

print(f"----- BOOKS IN {search_genre} -----")
for book in books:
    if book['genre'].lower() == search_genre.lower():
        print("ID:", book['id'])
        print("Title:", book['title'])
        print("Author:", book['author'])
        print("Copies:", book['copies'])
        print("-----------------------------------")
        found = True

if not found:
    print("No books found in this genre.")

# Borrow a book
book_id_to_borrow = input("Enter the Book ID to borrow:")
found = False
for b in books:
    if b['id'] == book_id_to_borrow:
        found = True
        if b['copies'] > 0:
            b['copies'] -= 1
            print("Book borrowed successfully")
        else:
            print("Sorry, this book is currently unavailable")
        break
if not found:
    print("Book not found")

# Return a book
book_id_to_return = input("Enter Book ID to return:")
found = False
for b in books:
    if b['id'] == book_id_to_return:
        b['copies'] += 1
        print("Book returned successfully")
        found = True
        break
if not found:
    print("Book not found") 

display_books()
lib_stats()