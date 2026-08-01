import pytest
from utils import api_client
from utils.assertions import *
from utils.data_provider import *
from utils.dynamic_payload_builder import build_user_payload, build_payload_list
from utils.logger import logger

# Load Datasets
json_data = get_json_data("create_users.json")
csv_data = get_csv_data("create_users.csv")
excel_data = get_excel_data("users.xlsx", sheet_name="CreateUsers")

# Generate Readable IDs for PyTest Execution Reports
json_ids = generate_test_ids(json_data, key_name="name")
csv_ids = generate_test_ids(csv_data, key_name="name")
excel_ids = generate_test_ids(excel_data, key_name="Name")

# Parametrized Tests for JSON Data
@pytest.mark.parametrize("raw_user", json_data, ids=json_ids)
@pytest.mark.api
def test_create_users_json_parametrized(api_session, raw_user):
    payload = build_user_payload(raw_user)
    response = api_client.post_request("/users", session=api_session, payload=payload)
    assert_status_code(response, 201)
    assert_response_time(response, max_seconds=2.0)

# Parametrized Tests for CSV Data
@pytest.mark.parametrize("raw_user", csv_data, ids=csv_ids)
@pytest.mark.api
def test_create_users_csv_parametrized(api_session, raw_user):
    payload = build_user_payload(raw_user)
    response = api_client.post_request("/users", session=api_session, payload=payload)
    assert_status_code(response, 201)
    assert_response_time(response, max_seconds=2.0)

# Parametrized Tests for Excel Data
@pytest.mark.parametrize("raw_user", excel_data, ids=excel_ids)
@pytest.mark.api
def test_create_users_excel_parametrized(api_session, raw_user):
    payload = build_user_payload(raw_user)
    response = api_client.post_request("/users", session=api_session, payload=payload)
    assert_status_code(response, 201)
    assert_response_time(response, max_seconds=2.0)