import pytest
import allure
from utils.api_client import delete
from utils.assertions import assert_status_code, assert_response_time

@allure.feature("User Management")
@allure.story("Delete User")
@pytest.mark.crud
def test_delete_user():
    response = delete("/users/2")
    
    assert_status_code(response, 204)
    assert_response_time(response)
    assert response.text == "", f"Expected empty response body, got {response.text}"