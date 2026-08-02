import json
import os

def read_json_file(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, "test_data", "json", file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)