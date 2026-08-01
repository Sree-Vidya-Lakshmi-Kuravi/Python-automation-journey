from utils.json_reader import get_test_data
from utils.csv_reader import get_csv_data
from utils.excel_reader import read_sheet_data
from utils.logger import logger


def get_data(file_type, file_name, sheet_name=None):
    """
    Unified interface to fetch data from JSON, CSV, or Excel files.
    
    :param file_type: "json", "csv", or "excel"
    :param file_name: Name of the file inside test_data/ directory (e.g., 'users.xlsx')
    :param sheet_name: Required ONLY if file_type is 'excel'
    :return: List of dictionaries representing rows/objects
    """
    if not file_type:
        logger.error("file_type argument cannot be empty")
        raise ValueError("file_type is required")

    file_type_clean = str(file_type).strip().lower()

    if file_type_clean == "json":
        logger.info(f"Unified Reader: Fetching JSON data from '{file_name}'")
        return get_test_data(file_name)

    elif file_type_clean == "csv":
        logger.info(f"Unified Reader: Fetching CSV data from '{file_name}'")
        return get_csv_data(file_name)

    elif file_type_clean == "excel":
        if not sheet_name:
            logger.error(f"Failed to read '{file_name}': sheet_name parameter is required for Excel files.")
            raise ValueError("sheet_name is required when file_type is 'excel'")
            
        logger.info(f"Unified Reader: Fetching Excel data from '{file_name}' [Sheet: '{sheet_name}']")
        return read_sheet_data(file_name, sheet_name)

    else:
        logger.error(f"Unsupported file_type: '{file_type}'. Must be 'json', 'csv', or 'excel'.")
        raise ValueError(f"Unsupported file_type: '{file_type}'. Supported formats: 'json', 'csv', 'excel'.")