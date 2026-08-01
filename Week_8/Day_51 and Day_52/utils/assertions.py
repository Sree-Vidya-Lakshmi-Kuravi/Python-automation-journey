from utils.logger import logger
from utils.schema_validator import validate_json_schema


def assert_status_code(response, expected_code: int):
    """
    Asserts that the response status code matches the expected status code.
    """
    actual_code = response.status_code
    assert actual_code == expected_code, (
        f"Expected status code {expected_code}, but got {actual_code}. "
        f"Response Body: {response.text}"
    )
    logger.info(f"Assertion Passed: Status code is {actual_code}")


def assert_response_time(response, max_seconds: float = 1.0):
    """
    Asserts that the response execution time is below the specified max threshold (in seconds).
    Example: max_seconds=0.5 (500 ms) or max_seconds=1.0 (1 second).
    """
    elapsed_seconds = response.elapsed.total_seconds()
    assert elapsed_seconds <= max_seconds, (
        f"Response time threshold exceeded! Expected <= {max_seconds}s, "
        f"but request took {elapsed_seconds:.3f}s"
    )
    logger.info(f"Assertion Passed: Response time {elapsed_seconds:.3f}s is within limit ({max_seconds}s)")


def assert_header(response, header_name: str, expected_value: str = None):
    """
    Asserts that a specific header exists in the response.
    If expected_value is provided, it asserts the value matches (case-insensitive key check).
    """
    headers_lower = {k.lower(): v for k, v in response.headers.items()}
    target_key = header_name.lower()

    assert target_key in headers_lower, (
        f"Header '{header_name}' missing from response headers. "
        f"Available headers: {list(response.headers.keys())}"
    )

    actual_value = headers_lower[target_key]

    if expected_value is not None:
        assert expected_value.lower() in actual_value.lower(), (
            f"Expected header '{header_name}' to contain '{expected_value}', "
            f"but got '{actual_value}'"
        )
        logger.info(f"Assertion Passed: Header '{header_name}' matches '{actual_value}'")
    else:
        logger.info(f"Assertion Passed: Header '{header_name}' exists in response")


def assert_cookie(response, cookie_name: str, expected_value: str = None):
    """
    Asserts that a cookie exists in the response cookies.
    Optionally checks the cookie value.
    """
    cookies = response.cookies.get_dict()
    assert cookie_name in cookies, (
        f"Cookie '{cookie_name}' not found in response cookies. "
        f"Available cookies: {list(cookies.keys())}"
    )

    if expected_value is not None:
        actual_value = cookies[cookie_name]
        assert actual_value == expected_value, (
            f"Expected cookie '{cookie_name}' to be '{expected_value}', but got '{actual_value}'"
        )
        logger.info(f"Assertion Passed: Cookie '{cookie_name}' matches expected value")
    else:
        logger.info(f"Assertion Passed: Cookie '{cookie_name}' exists")


def assert_json_value(data: dict | list, key_path: str, expected_value):
    """
    Navigates a nested JSON object using dot notation (e.g., 'data.id' or 'data.email')
    and asserts that the value matches expected_value.
    """
    keys = key_path.split(".")
    current = data

    for key in keys:
        if isinstance(current, dict):
            assert key in current, f"Nested key '{key}' from path '{key_path}' not found in response JSON"
            current = current[key]
        elif isinstance(current, list) and key.isdigit():
            idx = int(key)
            assert idx < len(current), f"Index {idx} out of range for list at path '{key_path}'"
            current = current[idx]
        else:
            raise AssertionError(f"Cannot navigate key '{key}' in non-dict/non-list object at path '{key_path}'")

    assert current == expected_value, (
        f"Value mismatch at JSON key path '{key_path}'! "
        f"Expected: '{expected_value}', Actual: '{current}'"
    )
    logger.info(f"Assertion Passed: JSON key path '{key_path}' matches '{expected_value}'")


def assert_json_schema(response_json: dict | list, schema_name: str):
    """
    Validates a response JSON object against a specified JSON schema file from schemas/.
    """
    validate_json_schema(response_json, schema_name)
    logger.info(f"Assertion Passed: Response JSON matches schema '{schema_name}'")