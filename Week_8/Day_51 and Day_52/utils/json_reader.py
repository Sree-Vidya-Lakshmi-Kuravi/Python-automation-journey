import json
import os
from utils.logger import logger

# Build dynamic absolute path to 'test_data' folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
TEST_DATA_DIR = os.path.join(PROJECT_ROOT, "test_data")


def load_json(file_path):
    """
    Reads any absolute JSON file path and returns Python dict/list.
    """
    if not os.path.exists(file_path):
        logger.error(f"JSON file not found at path: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        logger.info(f"Successfully read raw JSON from: {file_path}")
        return data


def get_test_data(file_name):
    """
    Fetches JSON content directly from the test_data/ directory by filename.
    Usage: get_test_data("create_users.json")
    """
    file_path = os.path.join(TEST_DATA_DIR, file_name)
    return load_json(file_path)