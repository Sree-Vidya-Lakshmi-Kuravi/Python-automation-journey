import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(login_fixture):

    assert "inventory" in login_fixture.current_url, "Login failed"
    print('Login success')


def test_invalid_login(browser_fixture):

    wait = WebDriverWait(browser_fixture, 10)
    browser_fixture.get("https://www.saucedemo.com")
    browser_fixture.find_element(By.ID, "user-name").send_keys("standard_user1")

    browser_fixture.find_element(By.ID, "password").send_keys("secret_sauce")

    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")))
    print(msg.text)

    assert "do not match" in msg.text, "Login success"
    print('Login failed')

