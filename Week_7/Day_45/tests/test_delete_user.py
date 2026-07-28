from utils.api_client import *

def test_delete_user():
    response = delete("users/5")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"