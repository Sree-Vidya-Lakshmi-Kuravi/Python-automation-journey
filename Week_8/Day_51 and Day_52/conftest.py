import pytest
import requests
from config.config_reader import *
from utils.logger import *
from utils.data_provider import get_data
from utils.dynamic_payload_builder import build_payload_list

@pytest.fixture(scope="session")
def api_session():
    logger.info("HTTP Session has started..")
    session = requests.Session()
    yield session
    logger.info("HTTP Session has closed..")
    session.close()

@pytest.fixture
def default_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Pytest-API-Automation/1.0"
    }

@pytest.fixture
def api_client(api_session, default_headers):
    logger.info("API Client has been initialized..")
    # Attach default headers directly to the session object
    api_session.headers.update(default_headers)
    # Pass the session object to the test functions
    yield api_session

def pytest_addoption(parser):
    """
    Adds a custom CLI flag: --data-source
    Usage: pytest --data-source=excel
    We can use --data-source to call different data sources i.e., json, csv, or excel for the same test cases from CLI.
    """
    parser.addoption(
        "--data-source", action="store", default="json", choices=["json", "csv", "excel"], help="Data source for tests: json, csv, or excel"
    )


@pytest.fixture(scope="session")
def selected_source(request):
    """
    Retrieves the data source passed via CLI flag (default: 'json').
    """
    return request.config.getoption("--data-source")


@pytest.fixture(scope="function")
def dataset_provider(selected_source):
    """
    Challenge 4 Fixture: Automatically loads and prepares API payloads 
    from whichever source was selected via CLI (--data-source=excel/csv/json).
    """
    if selected_source.lower() == "excel":
        raw_data = get_data("excel", "users.xlsx", sheet_name="CreateUsers")
    elif selected_source.lower() == "csv":
        raw_data = get_data("csv", "create_users.csv")
    else:
        raw_data = get_data("json", "create_users.json")

    # Dynamically build payloads
    payloads = build_payload_list(raw_data)
    return payloads