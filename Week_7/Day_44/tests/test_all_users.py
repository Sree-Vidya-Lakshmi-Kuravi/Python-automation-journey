import requests
import json

def test_all_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users_data = response.json()
    with open("users.json") as file:
        expected_users = json.load(file)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert len(users_data) == 10, f"Expected 10 users, but got {len(users_data)}"
    assert users_data == expected_users, f"Expected users data to be a list, but got {users_data}"