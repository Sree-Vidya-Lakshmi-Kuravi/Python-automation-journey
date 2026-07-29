import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_req_header():
    post_id = 2
    url = f"{BASE_URL}/{post_id}"

    # User-Agent header is used to identify who is making the request. 
    # Accept header is used to specify the media type(s) that the client is willing to receive from the server.
    # Content-Type header is used to indicate the media type of the resource being sent to the server.
    headers = {"User-Agent": "Pytest-Automation-Testing",
               "Accept": "application/json",
               "Content-Type": "application/json"}

    res = requests.get(url, headers=headers)
    data = res.json()

    # Assert status code
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # Assert post ID in the response data
    assert data["id"] == post_id, f"Expected post ID {post_id}, but got {data['id']}"

    # To see the headers returned by response data
    res = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    print(dict(res.headers))