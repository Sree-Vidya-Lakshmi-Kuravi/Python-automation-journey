from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_visibility(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((locator)))
        return element

    def wait_for_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator)))
        return element

    def wait_for_presence(self, locator):
        element = self.wait.until(EC.presence_of_element_located((locator)))
        return element

    def wait_for_eles_visibility(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located((locator)))
        return elements