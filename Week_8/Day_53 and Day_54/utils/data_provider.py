from utils.readers.json_reader import read_json_file
from utils.readers.csv_reader import read_csv_file
from utils.readers.excel_reader import read_excel_file
from config.config_reader import get_data_format

def get_test_data(file_key):
    file_format = get_data_format().lower()

    if file_format == "json":
        return read_json_file(f"{file_key}.json")
    elif file_format == "csv":
        return read_csv_file(f"{file_key}.csv")
    elif file_format == "excel":
        return read_excel_file(f"{file_key}.xlsx")
    else:
        raise ValueError(f"Unsupported format: {file_format}")