from selenium import webdriver
from config.config_reader import *
from utils.logger import CustomLogger

logger = CustomLogger.get_logger()

class DriverFactory:
    
    @staticmethod
    def get_driver():
        """Creating browser instance"""
        browser_name = ConfigReader.get_browser().lower().strip()

        if browser_name == "chrome":
            logger.info("Launching chrome..")
            driver = webdriver.Chrome()
        
        elif browser_name == "edge":
            logger.info("Launching edge..")
            driver = webdriver.Edge()
        
        else:
            logger.error(f"Unsupported browser: {browser_name}")
            raise ValueError(f"Unsupported browser: {browser_name}\nSupported browsers are: chrome, edge")

        """Maximizing the window"""
        driver.maximize_window()

        """Applying waits"""
        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        base_url = ConfigReader.get_base_url()
        logger.info(f"The base URL: {base_url} ")
        driver.get(base_url)

        return driver