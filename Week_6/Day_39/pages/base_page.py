from selenium import webdriver
from config.config_reader import ConfigReader
from utils.waits import *
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(self.driver, timeout = ConfigReader.get_explicit_wait())

    def wait_for_element(self, locator):
        """Waits for element to be visible and returns the element"""
        ele = self.wait.wait_for_visibility(locator)
        return ele

    def click(self, locator):
        """Waits for element until clicked and clicks it"""
        ele = self.wait.wait_for_clickable(locator)
        ele.click()

    def type_text(self, locator, text):
        """Waits for input field, clears the text, enters the input"""
        w = self.wait_for_element(locator)
        w.clear()
        w.send_keys(text)

    def get_text(self, locator):
        """Waits for element to be visible and returns the text"""
        w = self.wait_for_element(locator)
        return w.text

    def is_displayed(self, locator):
        """Returns True if the element is visible on screen, False otherwise."""
        try:
            return self.wait_for_element(locator).is_displayed()
        except TimeoutException:
            return False