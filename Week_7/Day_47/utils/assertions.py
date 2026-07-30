from utils.logger import logger

def assert_status_code(response, expected_code):
    """
    Validates the HTTP status code of a response.
    """
    actual_code = response.status_code
    logger.info(f"Asserting Status Code: Expected [{expected_code}], Got [{actual_code}]")
    assert actual_code == expected_code, (
        f"Status Code Mismatch! Expected: {expected_code}, but got: {actual_code}. "
        f"Response Body: {response.text}"
    )

def assert_key_exists(response_json, key):
    """
    Validates that a specific key exists in the JSON response.
    """
    logger.info(f"Asserting key '{key}' exists in response")
    assert key in response_json, f"Missing Key Error! Key '{key}' was not found in response: {response_json}"

def assert_field_value(response_json, key, expected_value):
    """
    Validates that a specific JSON field matches an expected value.
    """
    assert_key_exists(response_json, key)
    actual_value = response_json[key]
    logger.info(f"Asserting field '{key}': Expected [{expected_value}], Got [{actual_value}]")
    assert actual_value == expected_value, (
        f"Field Value Mismatch for key '{key}'! "
        f"Expected: '{expected_value}', but got: '{actual_value}'"
    )

def assert_response_time(response, max_seconds=2.0):
    """
    Validates that the API response time is within acceptable SLA limits.
    """
    # elapsed time is the time that has passed since the request was sent until the response was received
    elapsed_time = response.elapsed.total_seconds()
    logger.info(f"Asserting Response Time: Allowed max [{max_seconds}s], Actual [{elapsed_time:.2f}s]")
    
    # Performance SLA acts as the threshold for what is considered acceptable performance.
    assert elapsed_time <= max_seconds, (
        f"Performance SLA Violation! Response took {elapsed_time:.2f} seconds, "
        f"exceeding maximum limit of {max_seconds} seconds."
    )