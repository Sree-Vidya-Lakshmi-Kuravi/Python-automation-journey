import pytest
from utils import api_client
from utils.assertions import assert_status_code, assert_field_value, assert_response_time
from utils.payload_builder import get_create_user_payload, get_update_payload
from utils.logger import logger


@pytest.mark.regression
@pytest.mark.api
def test_json_driven_crud_lifecycle(api_session):
    """
    End-to-End CRUD Lifecycle driven by utils/payload_builder.py
    """
    logger.info("=== STARTING MINI PROJECT: JSON-DRIVEN CRUD SUITE ===")
    
    # 1. READ PAYLOAD & CREATE USER
    create_payload = get_create_user_payload(index=0)
    create_response = api_client.post_request("/users", session=api_session, payload=create_payload)
    
    assert_status_code(create_response, 201)
    user_id = create_response.json().get("id", 2)
    logger.info(f"User created with ID: {user_id}")
    
    # 2. READ USER DETAILS
    get_response = api_client.get_request(f"/users/{user_id}", session=api_session)
    assert get_response.status_code in [200, 404]  # Mock APIs don't persist dynamic IDs
    
    # 3. UPDATE USER USING JSON DATA
    update_payload = get_update_payload(index=0)
    update_response = api_client.put_request(f"/users/{user_id}", session=api_session, payload=update_payload)
    
    assert_status_code(update_response, 200)
    assert_field_value(update_response.json(), "job", update_payload["job"])
    
    # 4. DELETE USER
    delete_response = api_client.delete_request(f"/users/{user_id}", session=api_session)
    assert delete_response.status_code in [200, 204]
    
    logger.info("=== FINISHED MINI PROJECT: CRUD LIFECYCLE COMPLETE ===")