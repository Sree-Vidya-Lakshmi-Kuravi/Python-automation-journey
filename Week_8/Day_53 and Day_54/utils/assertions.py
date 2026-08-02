import os
import json
import jsonschema
from utils.logger import logger

def assert_status_code(response, expected_code):
    actual_code = response.status_code
    logger.info(f"Asserting Status Code: Actual={actual_code}, Expected={expected_code}")
    assert actual_code == expected_code, f"Expected status {expected_code}, got {actual_code}. Response Body: {response.text}"

def assert_response_time(response, max_allowed_ms=5000):
    actual_time = getattr(response, 'elapsed_ms', response.elapsed.total_seconds() * 1000)
    logger.info(f"Asserting Response Time: Actual={actual_time}ms, Max={max_allowed_ms}ms")
    assert actual_time <= max_allowed_ms, f"Response time {actual_time}ms exceeded threshold {max_allowed_ms}ms"

def assert_json_schema(response, schema_file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(base_dir, "schemas", schema_file_name)
    
    logger.info(f"Validating JSON Schema from file: {schema_file_name}")
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)
        
    try:
        response_json = response.json()
        jsonschema.validate(instance=response_json, schema=schema)
        logger.info("JSON Schema validation successful.")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Schema Validation Error: {err.message}")
        raise AssertionError(f"Schema validation failed for {schema_file_name}: {err.message}")

def assert_key_value(response_json, key, expected_value):
    logger.info(f"Asserting Key Value: Key='{key}', Expected='{expected_value}'")
    assert key in response_json, f"Key '{key}' missing from response JSON"
    assert str(response_json[key]) == str(expected_value), f"Expected {key}='{expected_value}', got '{response_json[key]}'"