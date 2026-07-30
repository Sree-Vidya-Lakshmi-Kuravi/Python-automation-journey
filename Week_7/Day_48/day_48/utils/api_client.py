import requests
from utils.logger import *
from config.config_reader import *

def send_request(method, endpoint, session, json = None, params = None, headers = None, **kwargs):
    # method: Tells the function whether to make a GET, POST, PUT, or DELETE call.
    # endpoint: The specific API path (e.g., /posts/1).
    # session: Receives our PyTest api_session fixture to reuse open TCP connections (making tests run much faster).
    # json / params / headers: Accepts optional payload bodies, URL parameters, or custom headers.
    # **kwargs: Catches any extra arguments a test might pass (like query parameters or files).

    # 1. Fetch default settings
    base_url = config_reader.get_url()
    timeout = config_reader.get_timeout()

    # 2. Construct full URL cleanly
    if endpoint.startswith("http"):
        full_url = endpoint
    else:
        full_url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    # 3. Determine execution strategy
    request_executor = session.request if session else requests.request

    # 4. Log outgoing request details
    logger.info(f"--> [OUTGOING REQUEST] {method.upper()} {full_url}")
    if params:
        logger.debug(f"    Params: {params}")
    if json:
        logger.debug(f"    Body Payload: {json}")

    # 5. Execute HTTP Request
    response = request_executor(
        method=method.upper(),
        url=full_url,
        json=json,
        params=params,
        headers=headers,
        timeout=timeout,
        **kwargs
    )

    # 6. Log incoming response details
    response_time_ms = round(response.elapsed.total_seconds() * 1000, 2)
    logger.info(f"<-- [INCOMING RESPONSE] Status: {response.status_code} | Time: {response_time_ms}ms")
    return response


def get_request(endpoint, session=None, params=None, **kwargs):
    return send_request("GET", endpoint, session=session, params=params, **kwargs)

def post_request(endpoint, session=None, payload=None, **kwargs):
    return send_request("POST", endpoint, session=session, json=payload, **kwargs)

def put_request(endpoint, session=None, payload=None, **kwargs):
    return send_request("PUT", endpoint, session=session, json=payload, **kwargs)

def patch_request(endpoint, session=None, payload=None, **kwargs):
    return send_request("PATCH", endpoint, session=session, json=payload, **kwargs)

def delete_request(endpoint, session=None, **kwargs):
    return send_request("DELETE", endpoint, session=session, **kwargs)