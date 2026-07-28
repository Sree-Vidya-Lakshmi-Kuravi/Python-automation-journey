from utils.api_client import *

def test_put_user():
    data = {
        "id": 5,
        "name": "siri",
        "username": "siri45",
        "email": "siri@gmail.com"
    }

    # UPDATE THE DATA OF THE USER WITH ID 1 USING THE PUT METHOD
    response = put("users/5", data)
    #print(response.json())
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    assert data == response.json(), f"Expected data is {data} but got {response.json()}"
