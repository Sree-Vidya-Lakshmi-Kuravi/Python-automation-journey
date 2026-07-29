import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://postman-echo.com/basic-auth"

def test_basic_auth():
    # 1. Define the username and password for basic authentication
    username = "postman"
    password = "password"

    # 2. Send GET request with basic authentication
    res = requests.get(BASE_URL, auth=HTTPBasicAuth(username, password))
    print(f"Request URL: {res.url}")  # Optional: Print the full request URL for debugging

    # 3. Validate Status Code FIRST
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # 4. Parse JSON data (data is a dictionary)
    data = res.json()

    # 5. Validate that the response contains the expected authenticated user information
    assert data["authenticated"] is True, "Expected authenticated to be True"


import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth



def test_basic_auth():
    BASE_URL = "https://postman-echo.com/basic-auth"
    # 1. Define the username and password for basic authentication
    username = "postman"
    password = "password"

    # 2. Send GET request with basic authentication
    res = requests.get(BASE_URL, auth=HTTPBasicAuth(username, password))
    print(f"Request URL: {res.url}")  # Optional: Print the full request URL for debugging

    # 3. Validate Status Code FIRST
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # 4. Parse JSON data (data is a dictionary)
    data = res.json()

    # 5. Validate that the response contains the expected authenticated user information
    assert data["authenticated"] is True, "Expected authenticated to be True"



def test_digest_auth():
    BASE_URL = "https://postman-echo.com/digest-auth"
    # 1. Define the username and password for digest authentication
    username = "postman"
    password = "password"

    # 2. Send GET request with digest authentication
    res = requests.get(BASE_URL, auth=HTTPDigestAuth(username, password))
    print(f"Request URL: {res.url}")  # Optional: Print the full request URL for debugging

    # 3. Validate Status Code FIRST
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # 4. Parse JSON data (data is a dictionary)
    data = res.json()

    # 5. Validate that the response contains the expected authenticated user information
    assert data["authenticated"] is True, "Expected authenticated to be True"