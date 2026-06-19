from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

from utils.reusable_func import * 


def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    wait_for_visibility(driver, (By.ID, "user-name")).send_keys(username)
    wait_for_visibility(driver, (By.ID, "password")).send_keys(password)

    # login button
    wait_for_clickable(driver, (By.ID, "login-button")).click()


def positive_login():
    with webdriver.Chrome() as driver:
        driver.maximize_window()

        login(driver, "standard_user", "secret_sauce")
        assert validate_url(driver.current_url, "inventory.html")
        take_screenshot(driver, "Positive_Login")

# positive_login()


def negative_login():
    with webdriver.Chrome() as driver:
        driver.maximize_window()

        login(driver, "bvns", "bvns")
        validate_url(driver.current_url, "inventory.html")

        output_msg = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
        res = wait_for_visibility(driver, output_msg)

        assert validate_text(res.text, "Epic sadface: Username and password do not match any user in this service")

        take_screenshot(driver, "Negative_Login")

# negative_login()


def logout():
    with webdriver.Chrome() as driver:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        login(driver, "standard_user", "secret_sauce")

        if validate_url(driver.current_url, "inventory.html"):
            side_menu = (By.ID, "react-burger-menu-btn")
            side_menu_ele = wait_for_clickable(driver, side_menu)
            side_menu_ele.click()

            logout_btn = (By.CSS_SELECTOR, "#logout_sidebar_link")
            logout_btn_ele = wait_for_clickable(driver, logout_btn)
            logout_btn_ele.click()

            if validate_url(driver.current_url, "https://www.saucedemo.com/"):
                print("Logged out successfully. Redirected to the login page")
            else:
                print("Unable to logout. Try again")
        else:
            print("Unable to logout. Try again")
# logout()

# ---------------------------------------------------------------------------


# with webdriver.Chrome() as driver:
#     driver.get("https://www.saucedemo.com/")
#     wait = WebDriverWait(driver, 10)

#     driver.maximize_window()

#     def positive_login(uname, pwd):
#         username = wait_for_visibility(driver, ID)
#         username.send_keys(uname)

#         password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
#         password.send_keys(pwd)

#         login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
#         login_btn.click()

#         driver.save_screenshot('./screenshots/positive_login.png')

#     positive_login("standard_user", "secret_sauce")  # positive login

#     def login_success_verify(uname, pwd, url):
#         unames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']

#         assert uname in unames and pwd == 'secret_sauce', "Your username and password are correct"

#         assert driver.current_url == url, f"Expected {url}, but got this {driver.current_url}"

#     # login_success_verify("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html")

#     def negative_login(uname, pwd):
#         username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
#         username.send_keys(uname)

#         password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
#         password.send_keys(pwd)

#         login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
#         login_btn.click()

#         driver.save_screenshot('./screenshots/negative_login.png')

#         msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")))
#         print(msg.text)


#     # negative_login("bvns", "bvns") # negative login


#     # actual = "Epic sadface: Username and password do not match any user in this service"

#     # msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")))
#     # print(msg.text)

#     def neg_login_verify(expected, actual):
#         assert expected == actual, f"Expected Message {expected} Actual Message {actual}"
    
#     # neg_login_verify(msg, actual)


#     def logout():
#         positive_login("standard_user", "secret_sauce")
#         side_menu = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
#         side_menu.click()
#         time.sleep(2)

#         logout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
#         logout_btn.click()

#         time.sleep(2)

#     logout()

#     def logout_validate(url):
#         assert driver.current_url == url, "Logout successful. Redirected to login page"
    
#     url = 'https://www.saucedemo.com/'
#     logout_validate(url)