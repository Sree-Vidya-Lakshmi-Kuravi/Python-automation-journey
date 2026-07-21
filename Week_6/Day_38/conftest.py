import pytest
from selenium import webdriver

@pytest.fixture
def browser_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()