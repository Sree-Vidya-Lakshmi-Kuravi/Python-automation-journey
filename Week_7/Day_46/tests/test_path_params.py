import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_path_params():
    target_post_id = 17

    # 1. Define path parameters
    url = f"{BASE_URL}/{target_post_id}/comments"

    # 2. Send GET request
    res = requests.get(url)
    print(f"Request URL: {res.url}")  

    # 3. Validate Status Code FIRST
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"

    # 4. Parse JSON data (data is a SINGLE post dictionary)
    posts = res.json()

    # 5. Check postId and email on the FIRST comment in the list
    first_post = posts[0]
    assert first_post["postId"] == target_post_id, f"Expected postId {target_post_id}, got {first_post['postId']}"

    assert "@" in first_post["email"], f"Expected valid email, got {first_post['email']}" 