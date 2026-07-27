import requests

def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/999"
    response = requests.get(url)

    assert response.status_code == 404, f"Expected status code 404 for invalid user, but got {response.status_code}"