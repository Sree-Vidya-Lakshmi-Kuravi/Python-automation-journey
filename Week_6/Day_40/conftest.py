import pytest
import time
from drivers.driver_factory import DriverFactory
from utils.logger import CustomLogger
from utils.screenshots import ScreenshotUtils

# Initialize singleton logger
logger = CustomLogger.get_logger()

@pytest.fixture
def browser_fixture(request):
    """Pytest fixture to manage browser lifecycle and calculate execution time."""
    start_time = time.time()
    test_name = request.node.name
    logger.info(f"🚀 Starting test execution: '{test_name}'")

    # 1. Initialize driver via DriverFactory
    driver = DriverFactory.get_driver()

    # 2. Attach driver to request.node so the failure hook can access it
    request.node.driver = driver

    # 3. Hand control over to the test function
    yield driver

    # 4. Teardown: Quit driver
    driver.quit()

    # Challenge 3: Calculate and log execution duration
    duration = round(time.time() - start_time, 2)
    logger.info(f"⏱️ Finished test '{test_name}' in {duration} seconds.\n" + "-"*60)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook wrapper to detect test failures and trigger screenshots."""
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only care about the actual test execution phase ('call')
    if rep.when == "call":
        test_name = item.name
        
        if rep.failed:
            # Challenge 1: Log failure and capture screenshot only on failure
            logger.error(f"❌ TEST FAILED: '{test_name}'")
            
            # Retrieve driver instance attached in browser_fixture
            driver = getattr(item, "driver", None)
            if driver:
                ScreenshotUtils.capture_ss(driver, test_name)
            else:
                logger.error(f"⚠️ Could not capture screenshot for '{test_name}': Driver instance not found.")
        
        elif rep.passed:
            logger.info(f"✅ TEST PASSED: '{test_name}'")