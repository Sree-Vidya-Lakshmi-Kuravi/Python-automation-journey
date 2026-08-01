from utils import json_reader, csv_reader, excel_reader

def get_json_data(file_name):
    return json_reader.get_test_data(file_name)

def get_csv_data(file_name):
    return csv_reader.get_csv_data(file_name)

def get_excel_data(file_name, sheet_name="CreateUsers"):
    return excel_reader.read_sheet_data(file_name, sheet_name)

def get_data(source, file_name, sheet_name=None):
    source = str(source).lower().strip()
    if source == "json":
        return get_json_data(file_name)
    elif source == "csv":
        return get_csv_data(file_name)
    elif source == "excel":
        sheet = sheet_name or "CreateUsers"
        return get_excel_data(file_name, sheet_name=sheet)
    else:
        raise ValueError(f"Unsupported source: {source}")

def generate_test_ids(data_list, key_name="Name"):
    ids = []
    for index, item in enumerate(data_list):
        val = item.get(key_name) or item.get(key_name.lower()) or item.get("Scenario") or item.get("scenario")
        if val:
            ids.append(f"{val}")
        else:
            ids.append(f"Row_{index + 1}")
    return ids