import time
import requests
import json
import allure
from utils.logger import logger
from config.config_reader import get_base_url, get_timeout, get_api_key

session = requests.Session()
session.headers.update({
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-key": get_api_key(),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

def send_request(method, endpoint, payload=None, params=None, headers=None):
    base_url = get_base_url().rstrip('/')
    formatted_endpoint = endpoint if endpoint.startswith('/') else f"/{endpoint}"
    url = f"{base_url}{formatted_endpoint}" if not endpoint.startswith("http") else endpoint
    
    request_headers = session.headers.copy()
    if headers:
        request_headers.update(headers)

    logger.info("========== OUTBOUND REQUEST ==========")
    logger.info(f"Method: {method.upper()} | URL: {url}")
    logger.info(f"Headers: {request_headers}")
    if params:
        logger.info(f"Query Params: {params}")
    if payload is not None:
        logger.info(f"Payload: {json.dumps(payload, indent=2)}")

    start_time = time.time()
    try:
        response = session.request(
            method=method.upper(),
            url=url,
            json=payload if payload is not None else None,
            params=params,
            headers=request_headers,
            timeout=get_timeout()
        )
        elapsed_time_ms = round((time.time() - start_time) * 1000, 2)
        
        logger.info("========== INBOUND RESPONSE ==========")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {elapsed_time_ms} ms")
        
        try:
            resp_json = response.json()
            logger.info(f"Response Body: {json.dumps(resp_json, indent=2)}")
        except Exception:
            logger.info(f"Response Raw Body: {response.text}")
        
        allure.attach(
            f"Method: {method}\nURL: {url}\nHeaders: {request_headers}\nPayload: {payload}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            f"Status: {response.status_code}\nTime: {elapsed_time_ms}ms\nBody: {response.text}",
            name="Response Details",
            attachment_type=allure.attachment_type.TEXT
        )

        response.elapsed_ms = elapsed_time_ms
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP Request failed: {str(e)}")
        raise e

def get(endpoint, params=None, headers=None):
    return send_request("GET", endpoint, params=params, headers=headers)

def post(endpoint, payload=None, headers=None):
    return send_request("POST", endpoint, payload=payload, headers=headers)

def put(endpoint, payload=None, headers=None):
    return send_request("PUT", endpoint, payload=payload, headers=headers)

def patch(endpoint, payload=None, headers=None):
    return send_request("PATCH", endpoint, payload=payload, headers=headers)

def delete(endpoint, headers=None):
    return send_request("DELETE", endpoint, headers=headers)