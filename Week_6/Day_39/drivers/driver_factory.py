from selenium import webdriver
from config.config_reader import *

class DriverFactory:
    @staticmethod
    def get_driver():
        """Creating browser instance"""
        browser_name = ConfigReader.get_browser().lower().strip()

        if browser_name == "chrome":
            driver = webdriver.Chrome()
        
        elif browser_name == "edge":
            driver = webdriver.Edge()
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}\nSupported browsers are: chrome, edge")

        """Maximizing the window"""
        driver.maximize_window()

        """Applying waits"""
        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        driver.get(ConfigReader.get_base_url())

        return driver