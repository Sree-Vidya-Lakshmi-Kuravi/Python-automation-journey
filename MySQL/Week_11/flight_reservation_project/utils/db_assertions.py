def assert_record_exists(res):
    assert res is not None, "Expecting a record to exist, got None"

def assert_record_count(count, min_count = 1):
    assert count >= min_count, f"Expected atleast {min_count} records, but got {count} records"

def assert_field_count(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"

def assert_no_duplicate(values):
    assert len(values) == len(set(values)), "Duplicate values found"