# Custom Exception Class
class ItemNotAvailableError(Exception):
    pass

# Parent Class
class Media:
    def __init__(self, title, creator, item_id):
        self.title = title
        self.creator = creator
        self.item_id = item_id
        self._is_checked = False

    def display_details(self):
        print("===== BOOK INFORMATION =====")
        print(f"Book Title: {self.title}")
        print(f"Book Creator: {self.creator}")
        print(f"Book ID: {self.item_id}")

    def borrow_item(self):
        if self._is_checked == True:
            raise ItemNotAvailableError(f"'{self.title}' Book is not available now..")
        else:
            self._is_checked = True
            print(f"'{self.title}' Book has been checked out now..")

    def return_item(self):
        self._is_checked = False
        print(f"'{self.title}' Book is available..") 


# Child Class
class Book(Media):
    def __init__(self, title, creator, item_id, page_count):
        super().__init__(title, creator, item_id)
        self.page_count = page_count

    def display_details(self):
        super().display_details()
        print(f"Book Page Count: {self.page_count}")


# Library class
class Library():
    def __init__(self, name):
        self.name = name
        self.catalog = []

    def add_item(self, media_item):
        self.catalog.append(media_item)
        return self.catalog

    def find_item(self, item_id):
        for c in self.catalog:
            if c.item_id == item_id:
                return c
        return None

    def checkout(self, item_id):
        f = self.find_item(item_id)
        if not f:
            print(f"Error: Item with ID '{item_id}' not found in catalog")
            return
        try:
            f.borrow_item()
        except ItemNotAvailableError as e:
            print(f"Checkout Failed: {e}")

    def return_media(self, item_id):
        r = self.find_item(item_id)
        if not r:
            print(f"Error: Item with ID '{item_id}' not found in catalog.")
            return
        r.return_item()


class AudioBook(Media):
    def __init__(self, title, creator, item_id, duration_hours, max_licenses = 2):
        super().__init__(title, creator, item_id)
        self.duration_hours = duration_hours
        self.max_licenses = max_licenses
        self.active_streams = 0

    def borrow_item(self):
        super().borrow_item()
        if self.active_streams >= self.max_licenses:
            raise ItemNotAvailableError(f"All {self.max_licenses} stream licenses for '{self.title}' are in use")
        else:
            self.active_streams += 1
            print(f"The active streams are {self.active_streams}")

    def return_item(self):
        super().return_item()
        if self.active_streams > 0:
            self.active_streams -= 1

    def display_details(self):
        super().display_details()
        print(f"The duration is - {self.duration_hours}\nThe available licenses is - {self.max_licenses}")


lib = Library("Public Library")
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K.Rowling", "HP001", 280)
abook1 = AudioBook("End of Beginning", "DJo", "E001", 1, 2)
lib.add_item(book1)
lib.add_item(abook1)

print("\n--- Displaying Details ---")
book1.display_details()
abook1.display_details()

lib.checkout("HP001")
lib.checkout("HP001")

print("\n --> Returning the Book and Checkout <--")
lib.return_media("HP001")
lib.checkout("HP001")

print("\n --> Audio Book <--")
lib.checkout("E001")
lib.checkout("E001")
lib.checkout("E001") # Exceeds maximum licenses

print("\n --> Return Audio Stream <--")
lib.return_media("E001")
lib.checkout("E001")

print("\n --> Testing Missing Item <--")
lib.checkout("00")