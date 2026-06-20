# validating the url
def validate_url(actual, expected):
    if expected not in actual:
        print(f"'{expected}' is not present in url '{actual}'")
        return False
    else:
        print(f"'{expected}' is present in url '{actual}'")
        return True


# validate text
def validate_text(actual, expected):
    if expected in actual:
        print(f"Text has been matched successfully.\n Actual text: {actual}\n Expected Text: {expected}")
        return True
    else:
        print(f"Text has not matched successfully.\n Actual text: {actual}\n Expected Text: {expected}")
        return True