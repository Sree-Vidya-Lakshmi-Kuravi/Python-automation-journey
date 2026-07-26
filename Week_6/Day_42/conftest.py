import pytest
import time
import os
from datetime import datetime
from drivers.driver_factory import DriverFactory
from utils.logger import CustomLogger
from utils.screenshots import ScreenshotUtils
from utils.report_cleanup import ReportCleanupUtils
from config.config_reader import ConfigReader

logger = CustomLogger.get_logger()

# Dynamic report naming (Challenge 1) & automatic cleanup (Challenge 2)
def pytest_configure(config):
    """
    Pytest hook executed before test runs.
    Handles old report cleanup, timestamped filename generation, and metadata assignment.
    """
    # 1. Challenge 2: Keep only the 5 latest reports
    ReportCleanupUtils.cleanup_old_reports(keep_count=5)

    # 2. Challenge 1: Dynamic timestamped report filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join("reports", "html", f"report_{timestamp}.html")
    
    # Programmatically assign report path
    config.option.htmlpath = report_path

    # 3. Safe Metadata Assignment (Supports pytest-html v3 and v4+)
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "SauceDemo E-Commerce Automation"
        config._metadata["Tester Name"] = "QA Engineer"
        config._metadata["Browser"] = ConfigReader.get_browser().upper()
        config._metadata["Environment"] = "QA / Staging"
        config._metadata["Execution Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@pytest.fixture
def browser_fixture(request):
    """Pytest fixture to manage browser lifecycle and calculate execution time."""
    start_time = time.time()
    test_name = request.node.name
    logger.info(f"🚀 Starting test execution: '{test_name}'")

    driver = DriverFactory.get_driver()
    request.node.driver = driver

    yield driver

    driver.quit()
    duration = round(time.time() - start_time, 2)
    logger.info(f"⏱️ Finished test '{test_name}' in {duration} seconds.\n" + "-"*60)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook wrapper to detect test failures and trigger screenshots."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        test_name = item.name
        
        if rep.failed:
            logger.error(f"❌ TEST FAILED: '{test_name}'")
            driver = getattr(item, "driver", None)
            if driver:
                ScreenshotUtils.capture_ss(driver, test_name)
            else:
                logger.error(f"⚠️ Could not capture screenshot for '{test_name}': Driver instance not found.")
        
        elif rep.passed:
            logger.info(f"✅ TEST PASSED: '{test_name}'")