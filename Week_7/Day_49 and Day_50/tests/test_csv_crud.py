import pytest
from utils import api_client
from utils.api_client import *
from utils.assertions import *
from utils.payload_builder import *
from utils.logger import *

@pytest.mark.regression
@pytest.mark.api
def test_crud_csv(api_session):
    # creating a payload
    create_payload = get_create_user_payload(index = 0, source = "csv")
    logger.info(f"Loaded csv created payload: {create_payload}")
    
    # POST
    create_res = api_client.post_request("/users", session = api_session, payload = create_payload)
    # assertions
    assert_status_code(create_res, 201)
    logger.info("Step 1 (POST): The user has been created successfully")

    target_id = 2 # since, we are using JSONPlaceHolder which is a mock api, we are using target id hardcoded

    # GET 
    get_res = api_client.get_request(f"/users/{target_id}", session = api_session)
    assert_status_code(get_res, 200)
    logger.info("Step 2 (GET): The user details has been fetched successfully")

    update_payload = get_update_payload(index = 0, source = "csv")
    logger.info(f"Loaded CSV Update Payload: {update_payload}")

    # PUT
    update_res = api_client.put_request(f"/users/{target_id}", session = api_session, payload = update_payload)
    assert_status_code(update_res, 200)
    assert_field_value(update_res.json(), "job", update_payload["job"])
    logger.info(f"Step 3 (PUT): The user with ID {target_id} has been updated successfully")

    # DELETE
    delete_res = api_client.delete_request(f"/users/{target_id}", session = api_session)
    assert delete_res.status_code in [200, 204], f"Unexpected Status Code: {delete_res.status_code}"
    logger.info(f"Step 4 (DELETE): The user with ID {target_id} has been deleted successfully")

    logger.info("=== CSV CRUD LIFECYCLE COMPLETED SUCCESSFULLY ===")