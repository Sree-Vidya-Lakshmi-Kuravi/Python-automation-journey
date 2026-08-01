import os
import csv
from utils.logger import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
CSV_DATA_DIR = os.path.join(PROJECT_DIR, "test_data")

def load_csv(file_path):
    if not os.path.exists(file_path):
        logger.error(f"CSV file not found at path: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, mode = 'r', encoding='utf-8') as file:
        if os.path.getsize(file_path) == 0:
            logger.error(f"CSV file is empty at path: {file_path}")
            raise ValueError("CSV file is empty")

        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError("CSV missing headers")

        data_list = []
        for row in reader:
            cleaned_row = {k.strip(): v.strip() for k, v in row.items() if k is not None}
            data_list.append(cleaned_row)
        logger.info(f"Number of rows read from CSV: {len(data_list)}")
    return data_list


def get_csv_data(file_name):
    target_file_path = os.path.join(CSV_DATA_DIR, file_name)
    return load_csv(target_file_path)