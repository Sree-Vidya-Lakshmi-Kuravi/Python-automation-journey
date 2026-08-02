import pytest
import requests
from config.config_reader import *
from utils.logger import *

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
    logger.info("API Client has been initialized")
    api_session.headers.update(default_headers)
    yield api_session


