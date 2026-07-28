from utils.api_client import *

def test_get_users():
    response = get("users")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
