from selenium.webdriver.common.by import By
from utils.waits import WaitUtils
from pages.base_page import BasePage

class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_msg = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, uname):
        """Enter the username using BasePage Class"""
        self.type_text(self.username, uname)

    def enter_password(self, pwd):
        """Enter the password using BasePage Class"""
        self.type_text(self.password, pwd)

    def click_login(self):
        """Clicks the login button"""
        self.click(self.login_btn)

    def get_error_msg(self):
        """Displays error msg if anything goes wrong"""
        return self.get_text(self.error_msg)
        
    def login(self, username, password):
        """Correct login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
