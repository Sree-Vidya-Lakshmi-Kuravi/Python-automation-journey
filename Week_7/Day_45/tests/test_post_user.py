from utils.api_client import *

def test_post_user():
    data = {
        "name": "bvns",
        "username": "bvns",
        "email": "bvns@gmail.com"
    }
    response = post("users", data = data)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"