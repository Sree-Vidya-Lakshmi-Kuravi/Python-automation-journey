## Requests Library

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

# Get the status code
print(response.status_code)

# Convert response to json
data = response.json()
print(data)

# Print usernames
for d in data:
    print("Name:", d['name'])
    print("Email:", d['email'])


# Fetching single user

response = requests.get('https://jsonplaceholder.typicode.com/users/4')
print(response.text)