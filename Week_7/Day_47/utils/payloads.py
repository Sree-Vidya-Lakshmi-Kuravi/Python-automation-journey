import json
import os
from utils.logger import logger

# Locate the root 'test_data' directory relative to this file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "test_data")


def load_payload(filename="users.json", key=None):
    """
    Reads a JSON payload file from the test_data/ folder 
    and returns a Python dictionary.
    
    :param filename: Name of the JSON file in test_data directory.
    :param key: Specific top-level key to fetch (e.g., 'create_user').
    :return: Dictionary containing payload data.
    """
    file_path = os.path.join(DATA_DIR, filename)

    # 1. Check if the file exists
    if not os.path.exists(file_path):
        logger.error(f"Test data file missing: {file_path}")
        raise FileNotFoundError(f"Data file '{filename}' was not found in: {DATA_DIR}")

    # 2. Open and parse JSON data
    with open(file_path, "r") as file:
        data = json.load(file)

    # 3. Fetch specific key if requested
    if key:
        if key not in data:
            logger.error(f"Payload key '{key}' not found in {filename}")
            raise KeyError(f"Key '{key}' was not found inside '{filename}'")
        
        logger.info(f"Successfully loaded payload key '{key}' from {filename}")
        return data[key]

    logger.info(f"Successfully loaded entire payload file: {filename}")
    return data