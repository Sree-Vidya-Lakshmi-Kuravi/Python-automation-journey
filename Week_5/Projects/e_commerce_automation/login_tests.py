from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()

    def positive_login(uname, pwd):
        username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys(uname)
        driver.implicitly_wait(3)

        password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys(pwd)
        driver.implicitly_wait(3)

        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        driver.implicitly_wait(3)

        driver.save_screenshot('./screenshots/positive_login.png')

    positive_login("standard_user", "secret_sauce")  # positive login

    def login_success_verify(uname, pwd, url):
        unames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']

        if uname in unames and pwd == 'secret_sauce':
            print("Your username and password are correct")
            if driver.current_url == url:
                print("Login Success")
            else:
                print("Login failed")
        else:
            print("Your username or password is wrong")

    # login_success_verify("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html")

    def negative_login(uname, pwd):
        username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys(uname)
        driver.implicitly_wait(3)

        password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys(pwd)
        driver.implicitly_wait(3)

        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        driver.implicitly_wait(3)

        driver.save_screenshot('./screenshots/negative_login.png')

        msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")))
        print(msg.text)


    # negative_login("bvns", "bvns") # negative login


    # actual = "Epic sadface: Username and password do not match any user in this service"

    # msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")))
    # print(msg.text)

    def neg_login_verify(expected, actual):
        if expected == actual:
            print("Login Failed Message has been displayed correctly")
        else:
            print("Something went wrong with the Login Failed Message")
    
    # neg_login_verify(msg, actual)


    def logout():
        positive_login("standard_user", "secret_sauce")
        side_menu = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        side_menu.click()
        time.sleep(2)

        logout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
        logout_btn.click()

        time.sleep(2)

    logout()

    def logout_validate(url):
        if driver.current_url == url:
            print("Logout successful. Redirected to login page")
        else:
            print("Not logged out successfully")
    
    url = 'https://www.saucedemo.com/'
    logout_validate(url)