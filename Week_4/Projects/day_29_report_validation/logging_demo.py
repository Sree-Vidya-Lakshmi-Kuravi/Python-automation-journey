from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def validate_msg(expected, actual):
    if expected == actual:
        return True
    return False


with webdriver.Chrome() as driver:
    driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 10)


    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")

    time.sleep(2)


    pwd = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    pwd.send_keys("SuperSecretPassword!")

    time.sleep(2)

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button")))
    login_btn.click()
    time.sleep(2)

    output = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    if validate_msg(output.text, 'Your username is invalid') or validate_msg(output.text, 'Your password is invalid'):
        print("Login failed")
        driver.save_screenshot('./day_29_report_validation/screenshots/login_failed.png')

    elif validate_msg(output.text,  'You logged into a secure area'):
        print("Login Success!!!")
        driver.save_screenshot('./day_29_report_validation/screenshots/login_success.png')

    else:
        print("Something went wrong")