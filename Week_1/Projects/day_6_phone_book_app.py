
## Phone Book Application

# Program should:
# add contact
# search contact
# delete contact
# display all contacts

print("-----------------------------------")
print("PHONE BOOK APPLICATION")
print("-----------------------------------")

c_book = [
    {'name': 'siri', 'phone': '8985325609'},
    {'name': 'mahi', 'phone': '7386355745'},
    {'name': 'ram', 'phone': '7670885108'}
]


print("==== Your Contacts ====")

for i in c_book:
    print("Name:", i['name'], "\n" ,"Phone Number:", i['phone'])


# add contact
def add_c():
    print()
    name = input("Enter the name: ")
    phone = int(input("Enter the phone number: "))

    c_book.append({'name': name, 'phone': phone})

    print("Your contact has been saved successfully.")

    print("Your updated contacts:")
    
    display_c()


# search contact
def search_c():
    print("\n1. Name\n2. Phone Number")
    y = int(input("Select how you want to search your contact:"))

    # search contact by name
    def search_c_n():
        name = input("Enter the name of the contact you want to search: ")
        found = False

        for i in c_book:
            if i['name'] == name:
                print("Contact Found")
                print("Name:",i['name'],"||","Contact Number:", i['phone'])
                found = True
                break

        if not found:
            print("No contact found")


    # search contact by phone number
    def search_c_p():
        phone = int(input("Enter the phone number of the contact you want to search: "))
        found1 = False

        for i in c_book:

            if i['phone'] == phone:
                print("Contact found")
                print("Name:",i['name'],"||","Contact Number:", i['phone'])
                found1 = True
                break
        
        if not found1:
            print("No contact found") 


    if y == 1:
        search_c_n()

    elif y == 2:
        search_c_p()
    
    else:
        print("Wrong Choice")


# delete contact
def del_c():
    print("\n1. Name\n2. Phone Number")
    x = int(input("Select how you want to delete your contact:"))

    # delete contact by name
    def del_c_n():
        name = input("Enter the name of the contact you want to delete: ")
        found3 = False
        for i in c_book:
            if i['name'] == name:
                c_book.remove(i)
                found3 = True

        print(f"Your contact {name} has been deleted successfully.")
        print("Your updated contact list is: ")
        display_c()

        if not found3:
            print("Contact not found")


    # delete contact by phone number
    def del_c_p():
        phone = input("Enter the phone number of the contact you want to delete: ")
        found4 = False

        for i in c_book:
            if i['phone'] == phone:
                c_book.remove(i)
                found4 = True

        print(f"Your contact {phone} has been deleted successfully.")
        print("Your updated contact list is: ")
        display_c()

        if not found4:
            print("Contact not found")

    if x == 1:
        del_c_n()

    elif x == 2:
        del_c_p()
    
    else:
        print("Wrong Choice")


# display all contacts
def display_c():
    for i in c_book:
        print("Name:",i['name'],"||","Contact Number:", i['phone'])


while True:
    print()
    print("User Operations")
    print("----------------")
    print()
    print("1. Add a new contact\n2. Search for a contact\n3. Delete a contact\n4. Display all contacts\n5. Exit")
    print()
    ch = int(input("Enter the choice to perform the operation: "))

    # choices
    if ch == 1:
        add_c()

    elif ch == 2:
        search_c()

    elif ch == 3:
        del_c()

    elif ch == 4:
        display_c()

    elif ch == 5:
        break

    else:
        print("Wrong Choice.")
