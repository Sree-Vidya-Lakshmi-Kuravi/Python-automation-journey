### User Data Fetcher

## Menu
# Fetch all users
# Fetch single users
# Exit

import requests


# All users

def fetch_all_users(url):
    response = requests.get(url)
    data = response.json()
    print("======================== LIST OF ALL USERS ======================== ")

    if len(data) >= 1:
        for d in data:
            print("--------------------------------------------------")
            print("User Id:", d.get('id'))
            print("Name:", d.get('name'))
            print("Username: ", d.get('username'))
            print('Email: ', d.get('email'))
            print('Address: ', d.get('address'))
            print('Phone: ', d.get('phone'))
            print('Website: ', d.get('website'))
            print('Company: ', d.get('company'))

    else:
        print("No data found")


# Single user

def fetch_single_user(url):
    u_id = int(input("Enter the user_id:"))
    url = f"{url}/{u_id}"
    response = requests.get(url)

    print("======================== DETAILS OF USER ======================== ")

    if response.status_code == 200:
        d = response.json()
    
        print("--------------------------------------------------")
        print("User Id:", d.get('id'))
        print("Name:", d.get('name'))
        print("Username:", d.get('username'))
        print("Email:", d.get('email'))
        print("Address:", d.get('address'))
        print("Phone:", d.get('phone'))
        print("Website:", d.get('website'))
        print("Company:", d.get('company'))

    else:
        print("User not found")


while True:

    try:

        url = 'https://jsonplaceholder.typicode.com/users' 

        print("------- USER DATA FETCHER -------")
        print("1. Fetch all Users\n2. Fetch single User\n3. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 3:
            break

        elif ch == 1:
            fetch_all_users(url)

        elif ch == 2:
            fetch_single_user(url)

        else:
            print("Wrong Choice")

    except ValueError:
        print("Your choices should be in input only")