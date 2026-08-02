import csv
import os

def read_csv_file(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, "test_data", "csv", file_name)
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "expected_status" in row:
                row["expected_status"] = int(row["expected_status"])
            data.append(row)
    return data