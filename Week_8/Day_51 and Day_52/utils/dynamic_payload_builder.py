from utils.logger import logger

def clean_raw_data(raw_data):
    if not isinstance(raw_data, dict):
        return raw_data  # Return if not a dictionary

    metadata_keys = {"scenario", "result", "statuscode", "status_code", "response_time", "responsetime"}
    cleaned_data = {k: v for k, v in raw_data.items() if k.lower() not in metadata_keys}
    return cleaned_data

def build_user_payload(raw_dict):
    """
    Dynamically constructs a standardized JSONPlaceholder payload:
    {"title": "...", "body": "...", "userId": 1}
    """
    if not raw_dict:
        return {}

    cleaned = clean_raw_data(raw_dict)

    # Key lookup strategy
    title_val = (
        cleaned.get("title") or 
        cleaned.get("name") or 
        cleaned.get("Name") or 
        "Default Title"
    )
    
    body_val = (
        cleaned.get("body") or 
        cleaned.get("job") or 
        cleaned.get("Job") or 
        "Default Body"
    )

    payload = {
        "title": str(title_val).strip(),
        "body": str(body_val).strip(),
        "userId": 1
    }

    return payload


def build_payload_list(raw_data_list):
    """
    Transforms a list of raw row dictionaries into a list of clean API payloads.
    """
    if not isinstance(raw_data_list, list):
        logger.error("build_payload_list expects a list of dictionaries")
        raise TypeError("raw_data_list must be a list")

    payloads = [build_user_payload(item) for item in raw_data_list]
    logger.info(f"Dynamic Payload Builder: Successfully generated {len(payloads)} payloads.")
    return payloads