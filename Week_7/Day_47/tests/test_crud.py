import pytest
import requests
from utils import api_client
from utils.logger import *
from utils.assertions import *
from utils.payloads import *

@pytest.mark.smoke
@pytest.mark.api
def test_create_user(api_session):
    """
    POST Request: Create a new user resource.
    """
    logger.info("--- STARTING TEST: test_create_user ---")
    
    # 1. Load payload from test_data/users.json
    payload = load_payload("users.json", key="create_user")
    
    # 2. Execute Request via api_client
    response = api_client.post_request("/users", session=api_session, payload=payload)
    
    # 3. Assertions
    assert_status_code(response, 201)
    assert_response_time(response, max_seconds=2.0)
    
    data = response.json()
    assert_field_value(data, "name", payload["name"])
    assert_field_value(data, "job", payload["job"])
    assert "id" in data, "Response body missing generated 'id' field"
    
    logger.info(f"Successfully created user with ID: {data['id']}")


@pytest.mark.smoke
@pytest.mark.api
def test_get_single_user(api_session):
    """
    GET Request: Fetch details of an existing user.
    """
    logger.info("--- STARTING TEST: test_get_single_user ---")
    
    response = api_client.get_request("/users/2", session=api_session)
    
    assert_status_code(response, 200)
    assert_response_time(response, max_seconds=1.5)
    
    body = response.json()
    
    # Asserting directly on top-level object
    assert_field_value(body, "id", 2)


@pytest.mark.regression
@pytest.mark.api
def test_update_user(api_session):
    """
    PUT Request: Complete update of a user resource.
    """
    logger.info("--- STARTING TEST: test_update_user ---")
    
    payload = load_payload("users.json", key="update_user")
    response = api_client.put_request("/users/2", session=api_session, payload=payload)
    
    assert_status_code(response, 200)
    assert_response_time(response, max_seconds=2.0)
    
    data = response.json()
    assert_field_value(data, "name", payload["name"])
    assert_field_value(data, "job", payload["job"])


@pytest.mark.regression
@pytest.mark.api
def test_partially_update_user(api_session):
    """
    PATCH Request: Partial update of a user resource field.
    """
    logger.info("--- STARTING TEST: test_partially_update_user ---")
    
    payload = load_payload("users.json", key="patch_user")
    response = api_client.patch_request("/users/2", session=api_session, payload=payload)
    
    assert_status_code(response, 200)
    assert_response_time(response, max_seconds=2.0)
    
    data = response.json()
    assert_field_value(data, "job", payload["job"])


@pytest.mark.smoke
@pytest.mark.api
def test_delete_user(api_session):
    """
    DELETE Request: Remove a user resource.
    """
    logger.info("--- STARTING TEST: test_delete_user ---")
    
    response = api_client.delete_request("/users/2", session=api_session)
    
    # JSONPlaceholder returns 204 No Content or 200 OK for successful deletes
    assert response.status_code in [200, 204], f"Unexpected status code: {response.status_code}"
    assert_response_time(response, max_seconds=1.5)


# =========================================================
# NEGATIVE TEST SCENARIOS
# =========================================================

@pytest.mark.negative
@pytest.mark.api
def test_get_non_existent_user(api_session):
    """
    Negative Scenario: GET request to a non-existent endpoint path.
    """
    logger.info("--- STARTING TEST: test_get_non_existent_user ---")
    
    response = api_client.get_request("/users/239999", session=api_session)
    assert_status_code(response, 404)


@pytest.mark.negative
@pytest.mark.api
def test_create_user_invalid_payload(api_session):
    """
    Negative Scenario: POST request with malformed or invalid payload.
    """
    logger.info("--- STARTING TEST: test_create_user_invalid_payload ---")
    
    payload = load_payload("users.json", key="invalid_user")
    response = api_client.post_request("/users", session=api_session, payload=payload)
    
    # Validates that the request was processed or safely handled
    assert response.status_code in [201, 400], f"Unexpected status code: {response.status_code}"