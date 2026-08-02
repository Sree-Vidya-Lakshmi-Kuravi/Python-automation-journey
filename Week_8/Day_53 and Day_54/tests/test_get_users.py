import pytest
import allure
from utils.api_client import get
from utils.assertions import assert_status_code, assert_response_time, assert_json_schema

@allure.feature("User Management")
@allure.story("Get List of Users")
@pytest.mark.crud
def test_get_users_list():
    response = get("/users?page=2")
    
    assert_status_code(response, 200)
    assert_response_time(response)
    assert_json_schema(response, "users_schema.json")
    
    body = response.json()
    assert len(body["data"]) > 0, "Users list is empty"