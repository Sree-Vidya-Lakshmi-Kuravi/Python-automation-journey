import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_query_params():
    target_user_id = 2
    target_id = 17

    # 1. Define query parameters
    params = {"userId": target_user_id,
              "id": target_id}

    # 2. Send GET request
    res = requests.get(BASE_URL, params=params)
    print(f"Request URL: {res.url}")  # Optional: Print the full request URL for debugging

    # 3. Validate Status Code FIRST
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # 4. Parse JSON data (data is a LIST of post dictionaries)
    posts = res.json()

    # 5. Validate that we received at least one post
    assert len(posts) > 0, "Expected at least one post in response data"

    # 6. Validate that EVERY post returned belongs to userId = 2
    for post in posts:
        assert post["userId"] == target_user_id, f"Expected userId {target_user_id}, but got {post['userId']}"
