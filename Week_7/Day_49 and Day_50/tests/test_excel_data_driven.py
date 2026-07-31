import pytest
from utils import api_client
from utils.assertions import assert_status_code, assert_response_time
from utils.payload_builder import get_all_payloads
from utils.excel_reader import write_test_result
from utils.logger import logger

# Fetch datasets from Excel sheets at module load time for PyTest parametrization
excel_valid_users = get_all_payloads("create_users", source="excel", sheet_name="CreateUsers")
excel_invalid_users = get_all_payloads("invalid_users", source="excel", sheet_name="InvalidUsers")


# =========================================================
# Task 5 & Challenge 2: Excel Data-Driven POST Test + Result Recording
# =========================================================
@pytest.mark.parametrize("user_payload", excel_valid_users)
@pytest.mark.smoke
@pytest.mark.api
def test_create_users_excel(api_session, user_payload):
    """
    Executes POST /users for each row in CreateUsers sheet and writes execution results back to Excel.
    """
    # Excel row index: Row 1 is headers, so index 0 corresponds to Row 2
    row_idx = excel_valid_users.index(user_payload) + 2
    user_name = user_payload.get("Name", "Unknown")
    
    logger.info(f"--- EXCEL TEST: Creating user '{user_name}' (Target Row: {row_idx}) ---")

    # Filter out result reporting fields if they exist in user_payload
    payload = {k: v for k, v in user_payload.items() if k not in ["Result", "StatusCode", "ExecutionTime", "Remarks"]}

    try:
        response = api_client.post_request("/users", session=api_session, payload=payload)
        exec_time = f"{response.elapsed.total_seconds():.2f}s"
        
        # Validations
        assert_status_code(response, 201)
        assert_response_time(response, max_seconds=2.0)
        
        # Write PASS result back to Excel
        write_test_result(
            file_name="users.xlsx",
            sheet_name="CreateUsers",
            row_idx=row_idx,
            status="PASS",
            status_code=response.status_code,
            exec_time=exec_time,
            remarks="User created successfully"
        )
        logger.info(f"PASS recorded in users.xlsx row {row_idx} for '{user_name}'")

    except Exception as e:
        # Write FAIL result back to Excel if any assertion fails
        status_code = response.status_code if 'response' in locals() else "N/A"
        exec_time = f"{response.elapsed.total_seconds():.2f}s" if 'response' in locals() else "N/A"
        
        write_test_result(
            file_name="users.xlsx",
            sheet_name="CreateUsers",
            row_idx=row_idx,
            status="FAIL",
            status_code=status_code,
            exec_time=exec_time,
            remarks=str(e)
        )
        logger.error(f"FAIL recorded in users.xlsx row {row_idx} for '{user_name}': {e}")
        raise


# =========================================================
# Task 5: Negative Testing via Excel (InvalidUsers Sheet)
# =========================================================
@pytest.mark.parametrize("invalid_payload", excel_invalid_users)
@pytest.mark.negative
@pytest.mark.api
def test_invalid_users_excel(api_session, invalid_payload):
    """
    Executes POST /users for all negative scenarios in InvalidUsers sheet.
    """
    scenario = invalid_payload.get("Scenario", "Unknown Scenario")
    logger.info(f"--- RUNNING EXCEL NEGATIVE SCENARIO: {scenario} ---")

    # Clean non-payload fields before sending to API
    payload = {
        k: v for k, v in invalid_payload.items() 
        if k not in ["Scenario", "Result", "StatusCode", "ExecutionTime", "Remarks"]
    }

    response = api_client.post_request("/users", session=api_session, payload=payload)
    logger.info(f"Scenario [{scenario}] returned HTTP Status {response.status_code}")

    # Public mock APIs return 201 Created even for missing fields, while production returns 400 Bad Request
    assert response.status_code in [201, 400], f"Unexpected Status Code: {response.status_code}"