from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def browser_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(browser_fixture, username):
    browser_fixture.get("https://www.saucedemo.com/")
    browser_fixture.find_element(By.ID, "user-name").send_keys(username)
    browser_fixture.find_element(By.ID, "password").send_keys("secret_sauce")
    browser_fixture.find_element(By.ID, "login-button").click()

    return browser_fixture