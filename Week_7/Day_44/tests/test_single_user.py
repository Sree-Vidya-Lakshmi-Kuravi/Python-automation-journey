import requests

def test_single_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    user_data = response.json()

    assert user_data["id"] == 1, f"Expected user ID 1, but got {user_data['id']}"
    assert user_data["email"] == "Sincere@april.biz", f"Expected email 'Sincere@april.biz', but got {user_data['email']}"
    assert user_data["name"] == "Leanne Graham", f"Expected name 'Leanne Graham', but got {user_data['name']}"