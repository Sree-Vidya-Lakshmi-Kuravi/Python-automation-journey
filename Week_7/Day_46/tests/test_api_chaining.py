import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_api_chaining_workflow():
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Pytest-API-Testing/1.0"
    }

    # ==========================================
    # STEP 1: CREATE RESOURCE (POST)
    # ==========================================
    create_payload = {
        "title": "Learning API Chaining",
        "body": "Building automated API test pipelines with PyTest.",
        "userId": 1
    }

    # The json= parameter automatically converts Python dictionaries into JSON text
    post_res = requests.post(BASE_URL, json=create_payload, headers=headers)
    
    # Validate 201 Created status code
    assert post_res.status_code == 201, f"Expected 201 Created, got {post_res.status_code}"

    created_data = post_res.json()
    
    # Extract the generated ID (101) to verify POST creation response
    created_id = created_data["id"]
    assert "id" in created_data, "Response missing generated 'id'"
    assert created_data["title"] == create_payload["title"]

    print(f"\n[STEP 1 SUCCESS] Created post with generated ID: {created_id}")

    # ==========================================
    # STEP 2: UPDATE RESOURCE (PUT)
    # ==========================================
    # JSONPlaceholder mock API only accepts updates for existing IDs (1-100)
    target_id = 1  # Using existing post ID to avoid 500 server errors on fake IDs
    
    update_payload = {
        "id": target_id,
        "title": "Learning API Chaining - UPDATED",
        "body": "Updated body content after successful creation.",
        "userId": 1
    }

    put_url = f"{BASE_URL}/{target_id}"
    put_res = requests.put(put_url, json=update_payload, headers=headers)

    # Validate 200 OK status code
    assert put_res.status_code == 200, f"Expected 200 OK, got {put_res.status_code}"

    updated_data = put_res.json()
    assert updated_data["title"] == update_payload["title"]
    assert updated_data["body"] == update_payload["body"]

    print(f"[STEP 2 SUCCESS] Updated post ID {target_id} successfully.")

    # ==========================================
    # STEP 3: DELETE RESOURCE (DELETE)
    # ==========================================
    delete_url = f"{BASE_URL}/{target_id}"
    delete_res = requests.delete(delete_url, headers=headers)

    # Validate 200 OK (or 204 No Content) status code
    assert delete_res.status_code in [200, 204], f"Expected 200 or 204, got {delete_res.status_code}"

    print(f"[STEP 3 SUCCESS] Deleted post ID {target_id} successfully.")