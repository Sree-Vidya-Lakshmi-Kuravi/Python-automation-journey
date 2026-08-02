import pytest
import allure
from utils.api_client import get, post
from utils.assertions import assert_status_code

@allure.feature("Negative Test Scenarios")
@allure.story("Invalid Endpoint 404")
@pytest.mark.negative
def test_invalid_endpoint():
    response = get("/invalid_endpoint_xyz")
    assert_status_code(response, 404)

@allure.feature("Negative Test Scenarios")
@allure.story("User Not Found 404")
@pytest.mark.negative
def test_user_not_found():
    response = get("/users/23")
    assert_status_code(response, 404)

@allure.feature("Negative Test Scenarios")
@allure.story("Login Unregistered Email")
@pytest.mark.negative
def test_login_unregistered_email():
    payload = {"email": "unknown@test.com"}
    response = post("/login", payload=payload)
    assert_status_code(response, 400)

@allure.feature("Negative Test Scenarios")
@allure.story("Empty Payload Login")
@pytest.mark.negative
def test_empty_payload_login():
    response = post("/login", payload={})
    assert_status_code(response, 400)