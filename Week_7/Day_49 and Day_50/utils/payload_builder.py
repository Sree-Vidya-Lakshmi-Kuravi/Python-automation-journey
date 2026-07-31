from utils.json_reader import get_test_data
from utils.csv_reader import get_csv_data
from utils.data_reader import get_data
from utils.logger import logger

# creating a private helper function to avoid the repetition of same code
def _fetch_data_by_source(file_prefix, source = "json", sheet_name = None):

    source = str(source).strip().lower()
    
    if source == "json":
        file_name = f"{file_prefix}.json"
    elif source == "csv":
        file_name = f"{file_prefix}.csv"
    elif source == "excel":
        file_name = "users.xlsx"
        if not sheet_name:
            if "create" in file_prefix:
                sheet_name = "CreateUsers"
            elif "update" in file_prefix:
                sheet_name = "UpdateUsers"
            elif "invalid" in file_prefix:
                sheet_name = "InvalidUsers"
            else:
                sheet_name = "CreateUsers"
    else:
        logger.error(f"Unsupported data source requested: {source}")
        raise ValueError(f"Invalid data source: '{source}'. Supported sources: 'json', 'csv', 'excel'.")

    return get_data(file_type = source, file_name = file_name, sheet_name = sheet_name)


def get_create_user_payload(index=0, source="json", sheet_name="CreateUsers"):
    """
    Fetches a single create user payload from JSON, CSV, or Excel by index.
    """
    data = _fetch_data_by_source("create_users", source=source, sheet_name=sheet_name)
    payload = data[index]
    logger.info(f"Fetched create payload at index [{index}] from source [{source}]: {payload}")
    return payload


def get_update_payload(index = 0, source = "json", sheet_name = "UpdateUsers"):
    data = _fetch_data_by_source("update_users", source = source, sheet_name = sheet_name)
    payload = data[index]
    logger.info(f"Fetched update payload at index [{index}] from source [{source}]: {payload}")
    return payload


def get_invalid_payload(index = 0, source = "json", sheet_name = "InvalidUsers"):
    data = _fetch_data_by_source("invalid_users", source = source, sheet_name = sheet_name)
    payload = data[index]
    logger.info(f"Fetched invalid payload at index [{index}] from source [{source}]: {payload}")
    return payload


def get_all_payloads(file_prefix, source = "json", sheet_name = None):
    return _fetch_data_by_source(file_prefix, source = source, sheet_name = sheet_name)