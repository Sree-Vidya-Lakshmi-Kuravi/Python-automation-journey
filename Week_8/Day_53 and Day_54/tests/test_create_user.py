import pytest
import allure
from utils.api_client import post
from utils.assertions import assert_status_code, assert_response_time, assert_json_schema, assert_key_value
from utils.payload_builder import build_user_payload
from utils.data_provider import get_test_data

@allure.feature("User Management")
@allure.story("Create New User")
@pytest.mark.crud
@pytest.mark.parametrize("data", get_test_data("crud_data"))
def test_create_user(data):
    payload = build_user_payload(name=data["name"], job=data["job"])
    response = post("/users", payload=payload)
    
    assert_status_code(response, data["expected_status"])
    assert_response_time(response)
    assert_json_schema(response, "create_user_schema.json")
    assert_key_value(response.json(), "name", data["name"])