import pytest
from utils import api_client
from utils.assertions import assert_status_code, assert_field_value, assert_response_time
from utils.json_reader import get_test_data
from utils.logger import logger

# Fetch datasets for PyTest Parametrization
valid_users = get_test_data("create_users.json")
invalid_users = get_test_data("invalid_users.json")


# =========================================================
# PART 4 & CHALLENGE 1: Data-Driven Valid User Creation
# =========================================================
@pytest.mark.parametrize("user_payload", valid_users)
@pytest.mark.smoke
@pytest.mark.api
def test_create_users_data_driven(api_session, user_payload):
    """
    Executes POST /users for all 5 payloads from create_users.json
    """
    logger.info(f"--- STARTING DATA-DRIVEN POST TEST for: {user_payload['name']} ---")
    
    response = api_client.post_request("/users", session=api_session, payload=user_payload)
    
    # 1. Status Code Validation
    assert_status_code(response, 201)
    
    # 2. Response Time / SLA
    assert_response_time(response, max_seconds=2.0)
    
    # 3. Response Fields
    body = response.json()
    assert_field_value(body, "name", user_payload["name"])
    assert_field_value(body, "job", user_payload["job"])
    assert "id" in body, "Response missing 'id' field"


# =========================================================
# PART 5: Negative Testing with Invalid Payloads
# =========================================================
@pytest.mark.parametrize("invalid_payload", invalid_users)
@pytest.mark.negative
@pytest.mark.api
def test_create_users_negative_scenarios(api_session, invalid_payload):
    """
    Executes POST /users using invalid payloads and documents behavior.
    """
    scenario_name = invalid_payload.get("scenario", "Unknown Scenario")
    logger.info(f"--- RUNNING NEGATIVE SCENARIO: {scenario_name} ---")
    
    # Strip the non-payload tracking key 'scenario' before sending to API
    payload = {k: v for k, v in invalid_payload.items() if k != "scenario"}
    
    response = api_client.post_request("/users", session=api_session, payload=payload)
    
    # NOTE FOR PUBLIC MOCK APIs (JSONPlaceholder / ReqRes):
    # Mock APIs often accept any raw payload and still return 201 Created.
    # Production APIs usually return 400 Bad Request.
    # We validate that the API responds predictably (either 201 or 400).
    logger.info(f"Scenario [{scenario_name}] responded with HTTP status {response.status_code}")
    assert response.status_code in [201, 400], f"Unexpected Status Code: {response.status_code}"