import pytest
from utils import api_client
from utils.assertions import assert_status_code, assert_field_value, assert_response_time
from utils.payloads import load_payload
from utils.logger import logger


@pytest.mark.smoke
@pytest.mark.api
def test_get_users_list_pagination(api_session):
    """
    GET Request: Validate query parameters (_page and _limit) for users list.
    """
    logger.info("--- STARTING TEST: test_get_users_list_pagination ---")
    
    # JSONPlaceholder uses _page and _limit query parameters
    query_params = {"_page": 2, "_limit": 5}
    response = api_client.get_request("/users", session=api_session, params=query_params)
    
    assert_status_code(response, 200)
    assert_response_time(response, max_seconds=1.5)
    
    body = response.json()
    assert isinstance(body, list), f"Expected response to be a list, but got {type(body)}"
    assert len(body) > 0, "Users list should not be empty"


@pytest.mark.smoke
@pytest.mark.api
def test_get_single_user(api_session):
    """
    GET Request: Fetch details of a single user.
    """
    logger.info("--- STARTING TEST: test_get_single_user ---")
    
    response = api_client.get_request("/users/2", session=api_session)
    
    assert_status_code(response, 200)
    assert_response_time(response, max_seconds=1.5)
    
    body = response.json()
    assert_field_value(body, "id", 2)


@pytest.mark.regression
@pytest.mark.api
def test_create_and_verify_user(api_session):
    """
    POST Request: Create a new user resource.
    """
    logger.info("--- STARTING TEST: test_create_and_verify_user ---")
    
    payload = load_payload("users.json", key="create_user")
    response = api_client.post_request("/users", session=api_session, payload=payload)
    
    assert_status_code(response, 201)
    
    body = response.json()
    assert_field_value(body, "name", payload["name"])
    assert "id" in body, "Response body missing generated 'id' field"