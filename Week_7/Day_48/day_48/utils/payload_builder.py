from utils.json_reader import get_test_data
from utils.logger import logger


def get_create_user_payload(index=0):
    """
    Fetches a specific valid create user payload by list index.
    """
    data = get_test_data("create_users.json")
    payload = data[index]
    logger.info(f"Fetched create user payload at index [{index}]: {payload}")
    return payload


def get_update_payload(index=0):
    """
    Fetches an update user payload by list index.
    """
    data = get_test_data("update_users.json")
    payload = data[index]
    logger.info(f"Fetched update user payload at index [{index}]: {payload}")
    return payload


def get_invalid_payload(index=0):
    """
    Fetches an invalid payload scenario by list index.
    """
    data = get_test_data("invalid_users.json")
    payload = data[index]
    logger.info(f"Fetched invalid payload scenario at index [{index}]: {payload}")
    return payload  