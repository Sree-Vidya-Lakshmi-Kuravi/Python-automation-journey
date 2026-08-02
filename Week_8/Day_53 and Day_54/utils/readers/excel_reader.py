import os
import pandas as pd

def read_excel_file(file_name, sheet_name="Sheet1"):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, "test_data", "excel", file_name)
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    data = df.to_dict(orient="records")
    for row in data:
        if "expected_status" in row and pd.notna(row["expected_status"]):
            row["expected_status"] = int(row["expected_status"])
    return data