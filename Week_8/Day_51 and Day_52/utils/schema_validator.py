import json
from pathlib import Path
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
from utils.logger import logger

# Dynamic path resolution to the schemas/ directory
PROJECT_ROOT = Path(__file__).parent.parent
SCHEMAS_DIR = PROJECT_ROOT / "schemas"


def load_schema(schema_name: str) -> dict:
    """
    Loads a JSON schema file from the schemas/ directory.
    """
    # Append .json extension if not provided
    if not schema_name.endswith(".json"):
        schema_name += ".json"

    schema_path = SCHEMAS_DIR / schema_name

    if not schema_path.exists():
        logger.error(f"Schema file not found at path: {schema_path}")
        raise FileNotFoundError(f"Schema file '{schema_name}' does not exist in {SCHEMAS_DIR}")

    try:
        with open(schema_path, "r", encoding="utf-8") as file:
            schema_data = json.load(file)
            logger.debug(f"Successfully loaded schema: {schema_name}")
            return schema_data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in schema file '{schema_name}': {e}")
        raise ValueError(f"Schema file '{schema_name}' contains invalid JSON: {e}")


def validate_json_schema(response_json: dict | list, schema_name: str) -> bool:
    """
    Validates a response JSON object against a specified schema file.
    Challenge 1 & 2: Reusable schema validation tool reading from schemas/.
    """
    schema = load_schema(schema_name)

    try:
        validate(instance=response_json, schema=schema)
        logger.info(f"JSON Schema Validation PASSED for schema: {schema_name}")
        return True

    except ValidationError as err:
        error_msg = f"JSON Schema Validation FAILED [{schema_name}] -> Path '{list(err.path)}': {err.message}"
        logger.error(error_msg)
        raise AssertionError(error_msg) from err

    except SchemaError as err:
        error_msg = f"Invalid Schema Definition in '{schema_name}': {err.message}"
        logger.error(error_msg)
        raise SchemaError(error_msg) from err