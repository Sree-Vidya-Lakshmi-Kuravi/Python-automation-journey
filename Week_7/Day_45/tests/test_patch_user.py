from utils.api_client import *

def test_patch_user():
    data = {
        "id": 5,
        "name": "siri"
    }

    response = patch("users/5", data)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"