import pytest
from utils import api_client
from utils.api_client import *
from utils.assertions import *
from utils.payload_builder import *
from utils.logger import *

csv_valid_users = get_all_payloads("create_users", source = "csv")
csv_invalid_users = get_all_payloads("invalid_users", source = "csv")

@pytest.mark.parametrize("user_payload", csv_valid_users)
def test_create_users_csv_positive(api_session, user_payload):
    logger.info(f"Test execution has started with name: {user_payload['name']}")

    response = api_client.post_request("/users", session = api_session, payload = user_payload)

    assert_status_code(response, 201)
    assert_response_time(response, max_seconds = 2.0)

    data = response.json()
    assert_field_value(data, "name", user_payload['name'])
    assert_field_value(data, "job", user_payload['job'])
    assert "id" in data, "Response data is missing generating 'id field"


@pytest.mark.parametrize("invalid_payload", csv_invalid_users)
@pytest.mark.negative
@pytest.mark.api
def test_create_users_csv_negative(api_session, invalid_payload):
    scenario_name = invalid_payload.get("scenario", "Unknown Scenario")
    logger.info(f"Negative Scenario Test execution has started: {scenario_name}")

    payload = {k: v for k, v in invalid_payload.items() if k != "scenario"}
    
    response = api_client.post_request("/users", session=api_session, payload=payload)
    
    logger.info(f"Scenario [{scenario_name}] responded with HTTP status {response.status_code}")

    assert response.status_code in [201, 400], f"Unexpected Status Code: {response.status_code}"