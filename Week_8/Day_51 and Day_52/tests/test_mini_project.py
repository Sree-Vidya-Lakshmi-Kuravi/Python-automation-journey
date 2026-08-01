import pytest
from config.config_reader import BASE_URL
from utils.data_provider import get_data
from utils.dynamic_payload_builder import build_user_payload

# 1. Fetch datasets from all sources
json_data = get_data("json", "create_users.json")
csv_data = get_data("csv", "create_users.csv")
excel_data = get_data("excel", "users.xlsx", sheet_name="CreateUsers")

# 2. Combine datasets into tuples: (source_label, raw_row)
all_sources_data = (
    [("JSON", row) for row in json_data] +
    [("CSV", row) for row in csv_data] +
    [("Excel", row) for row in excel_data]
)

# 3. Create readable IDs: "JSON-Alice", "CSV-Bob", "Excel-Charlie"
multi_source_ids = []
for source, row in all_sources_data:
    name = row.get("name") or row.get("Name") or row.get("title") or "User"
    multi_source_ids.append(f"{source}-{name}")


# 4. Master Parametrized Test
@pytest.mark.parametrize("source, raw_user", all_sources_data, ids=multi_source_ids)
@pytest.mark.smoke
@pytest.mark.api
def test_create_user_all_sources(api_client, source, raw_user):
    """
    Option 2 with JSONPlaceholder: Uses full URL (BASE_URL/posts) with raw requests session.
    """
    # Build clean JSONPlaceholder payload
    payload = build_user_payload(raw_user)
    
    # Construct full URL for JSONPlaceholder (/posts)
    url = f"{BASE_URL}/posts"
    
    # Send HTTP POST request
    response = api_client.post(url, json=payload)

    # Assertions
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    assert response.elapsed.total_seconds() < 3.0, "Response time exceeded limit"

    body = response.json()
    assert body.get("title") == payload["title"]
    assert body.get("body") == payload["body"]
    assert "id" in body, "Response missing generated 'id' field"