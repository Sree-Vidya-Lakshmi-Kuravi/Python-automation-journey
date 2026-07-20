from selenium.webdriver.common.by import By
from utils.waits import WaitUtils

class LoginPage:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_msg = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(self.driver, timeout = 10)

    def enter_username(self, username):
        uname = self.wait.wait_for_visibility(self.username)
        uname.send_keys(username)

    def enter_password(self, password):
        pwd = self.wait.wait_for_visibility(self.password)
        pwd.send_keys(password) 

    def click_login(self):
        self.wait.wait_for_clickable(self.login_btn)

    def get_error_msg(self):
        err = self.wait.wait_for_visibility(self.error_msg)
        return err.text 
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
