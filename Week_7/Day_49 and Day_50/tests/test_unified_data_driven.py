import pytest
from utils import api_client
from utils.assertions import assert_status_code, assert_response_time
from utils.payload_builder import get_all_payloads
from utils.logger import logger

# =====================================================================
# MASTER DATA SOURCE SWITCH: Set to "json", "csv", or "excel"
# =====================================================================
DATA_SOURCE = "excel"


# Dynamic dataset loading based on the selected DATA_SOURCE
if DATA_SOURCE.lower() == "excel":
    unified_users = get_all_payloads("create_users", source = DATA_SOURCE, sheet_name = "CreateUsers")
else:
    unified_users = get_all_payloads("create_users", source = DATA_SOURCE)


# =====================================================================
# Day 50 Mini Project: Unified Data-Driven Test Suite
# =====================================================================
@pytest.mark.parametrize("user_payload", unified_users)
@pytest.mark.smoke
@pytest.mark.api
def test_create_user_unified(api_session, user_payload):
    """
    Executes POST /users using whichever data source is configured in DATA_SOURCE.
    Supports JSON, CSV, and Excel without changing any test logic!
    """
    # Normalize dictionary keys (JSON/CSV use 'name'/'job', Excel uses 'Name'/'Job')
    name = user_payload.get("name") or user_payload.get("Name")
    job = user_payload.get("job") or user_payload.get("Job")
    
    logger.info(f"--- UNIFIED TEST [{DATA_SOURCE.upper()}]: Creating user '{name}' ({job}) ---")
    
    payload = {"name": name, "job": job}
    
    # Send API request
    response = api_client.post_request("/users", session = api_session, payload = payload)
    
    # Validate Response Status Code and Response Time
    assert_status_code(response, 201)
    assert_response_time(response, max_seconds=2.0)
    
    # Validate Payload Integrity
    body = response.json()
    assert body.get("name") == name, f"Expected name '{name}', got '{body.get('name')}'"
    assert body.get("job") == job, f"Expected job '{job}', got '{body.get('job')}'"
    assert "id" in body, "Response body missing generated 'id' field"

    logger.info(f"SUCCESS [{DATA_SOURCE.upper()}]: User '{name}' verified with ID {body.get('id')}")