import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint, params = None):
    return requests.get(f"{BASE_URL}/{endpoint}", params = params)

def post(endpoint, data = None):
    return requests.post(f"{BASE_URL}/{endpoint}", data = data)

def put(endpoint, data):
    return requests.put(f"{BASE_URL}/{endpoint}", data = data)

def delete(endpoint, data = None):
    return requests.delete(f"{BASE_URL}/{endpoint}", data = data)

def patch(endpoint, data):
    return requests.patch(f"{BASE_URL}/{endpoint}", data = data)
