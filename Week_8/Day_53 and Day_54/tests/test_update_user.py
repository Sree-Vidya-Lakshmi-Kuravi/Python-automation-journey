import pytest
import allure
from utils.api_client import put, patch
from utils.assertions import assert_status_code, assert_response_time, assert_key_value
from utils.payload_builder import build_user_payload

@allure.feature("User Management")
@allure.story("Update User via PUT")
@pytest.mark.crud
def test_update_user_put():
    payload = build_user_payload(name="morpheus", job="zion resident")
    response = put("/users/2", payload=payload)
    
    assert_status_code(response, 200)
    assert_response_time(response)
    assert_key_value(response.json(), "job", "zion resident")

@allure.feature("User Management")
@allure.story("Partial Update User via PATCH")
@pytest.mark.crud
def test_update_user_patch():
    payload = build_user_payload(job="matrix agent")
    response = patch("/users/2", payload=payload)
    
    assert_status_code(response, 200)
    assert_response_time(response)
    assert_key_value(response.json(), "job", "matrix agent")