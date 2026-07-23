from selenium.webdriver.common.by import By
from utils.waits import *
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    checkout_btn = (By.ID, "checkout")
    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    zipcode = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    complete_header = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout(self):
        self.click(self.checkout_btn)

    def enter_first_name(self, f_name):
        self.type_text(self.firstname, f_name)

    def enter_last_name(self, l_name):
        self.type_text(self.lastname, l_name)

    def enter_zip_code(self, z_code):
        self.type_text(self.zipcode, z_code)

    def continue_checkout(self):
        self.click(self.continue_btn)

    def finish_checkout(self):
        self.click(self.finish_btn)

    def get_thank_you_msg(self):
        return self.get_text(self.complete_header)

