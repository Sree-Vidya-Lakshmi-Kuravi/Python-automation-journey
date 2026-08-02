import pytest
import allure
from utils.api_client import post
from utils.assertions import assert_status_code, assert_json_schema, assert_key_value
from utils.payload_builder import build_login_payload
from utils.data_provider import get_test_data

@allure.feature("Authentication")
@allure.story("Login Workflow")
@pytest.mark.auth
@pytest.mark.parametrize("data", get_test_data("login_data"))
def test_login_success(data):
    payload = build_login_payload(email=data["email"], password=data["password"])
    response = post("/login", payload=payload)
    
    assert_status_code(response, data["expected_status"])
    assert_json_schema(response, "login_schema.json")
    assert "token" in response.json()

@allure.feature("Authentication")
@allure.story("Login Missing Password")
@pytest.mark.auth
@pytest.mark.negative
def test_login_missing_password():
    payload = build_login_payload(email="peter@klaven")
    response = post("/login", payload=payload)
    
    assert_status_code(response, 400)
    assert_key_value(response.json(), "error", "Missing password")