import os
from datetime import datetime
from utils.logger import CustomLogger

# Getting the singleton logger 
logger = CustomLogger.get_logger()

class ScreenshotUtils:
    @staticmethod

    def capture_ss(driver, test_name):
        try:
            # Generate date string for creating the folder for a particular day
            today = datetime.now().strftime("%Y-%m-%d")

            # Define the path
            ss_dir = os.path.join("screenshots", today)
            os.makedirs(ss_dir, exist_ok=True)

            # Generate timestamped file
            time_stamp = datetime.now().strftime("%H-%M-%S")
            file_name = f"{test_name}_failed_{time_stamp}.png"

            # Full file path
            file_path = os.path.join(ss_dir, file_name)

            # Save screenshot
            driver.save_screenshot(file_path)
            logger.info(f"Screenshot captured successfully and saved to: {file_path}")
            return file_path

        except Exception as e:
            logger.error(f"Failed to capture the screeshot for test {test_name}: {e}")
            return None