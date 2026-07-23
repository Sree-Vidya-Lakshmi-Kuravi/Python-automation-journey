import pytest
from drivers.driver_factory import DriverFactory

@pytest.fixture
def browser_fixture():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()
