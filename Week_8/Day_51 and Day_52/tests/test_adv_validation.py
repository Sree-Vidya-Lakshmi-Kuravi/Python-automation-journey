import pytest
from config.config_reader import BASE_URL
from utils.assertions import (
    assert_status_code,
    assert_response_time,
    assert_header,
    assert_json_value,
    assert_json_schema
)
from utils.dynamic_payload_builder import build_user_payload


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_post_validation(api_client):
    """
    Mini Project Test 1: GET Single Resource
    Validates Status Code, Response Time (< 1.0s), Headers, Schema, and Nested Values.
    """
    url = f"{BASE_URL}/posts/1"
    response = api_client.get(url)

    # 1. Status Code Validation
    assert_status_code(response, 200)

    # 2. Response Time Validation (< 1 second / 1000 ms)
    assert_response_time(response, max_seconds=1.0)

    # 3. Header Validation
    assert_header(response, "Content-Type", expected_value="application/json")

    # 4. JSON Body Fields & Values Validation
    response_json = response.json()
    assert_json_value(response_json, "id", 1)
    assert_json_value(response_json, "userId", 1)

    # 5. Schema Validation (Challenge 1 & 2 & 3)
    # Note: If testing ReqRes /users/2, use "user_schema.json"
    assert_json_schema(response_json, "user_schema.json")


@pytest.mark.api
def test_get_posts_list_validation(api_client):
    """
    Mini Project Test 2: GET List Resource
    Validates array response structures, status codes, response times, and schemas.
    """
    url = f"{BASE_URL}/posts"
    response = api_client.get(url)

    # 1. Status Code Validation
    assert_status_code(response, 200)

    # 2. Response Time Validation (< 1.5 seconds)
    assert_response_time(response, max_seconds=1.5)

    # 3. Header Validation
    assert_header(response, "Content-Type", expected_value="json")

    # 4. JSON Array Body Validation
    response_json = response.json()
    assert isinstance(response_json, list), "Response should be a JSON Array"
    assert len(response_json) > 0, "List should not be empty"

    # Validate individual items in array
    first_item = response_json[0]
    assert_json_value(first_item, "id", 1)


@pytest.mark.api
def test_post_create_user_validation(api_client):
    """
    Mini Project Test 3: POST Resource Creation
    Validates creation payload, returned headers, response time, and creation schema.
    """
    url = f"{BASE_URL}/posts"
    raw_user_data = {"name": "Test Engineer", "job": "Automation Specialist"}
    payload = build_user_payload(raw_user_data)

    response = api_client.post(url, json=payload)

    # 1. Status Code Validation (201 Created)
    assert_status_code(response, 201)

    # 2. Response Time Validation (< 1.0 second)
    assert_response_time(response, max_seconds=1.0)

    # 3. Header Validation
    assert_header(response, "Content-Type", expected_value="json")

    # 4. Response Body & Value Assertions
    response_json = response.json()
    assert_json_value(response_json, "title", payload["title"])
    assert_json_value(response_json, "body", payload["body"])

    # 5. Creation Schema Validation
    assert_json_schema(response_json, "post_user_schema.json")