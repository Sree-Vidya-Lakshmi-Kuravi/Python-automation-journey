from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.reusable_func import *

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set default level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/automation.log"),  # Save logs to a file
        logging.StreamHandler()               # Also show logs in console
    ])


with webdriver.Chrome() as driver:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    def e_2_e_flow():
        try:
            # Login
            uname = driver.find_element(By.ID, "user-name")
            uname.send_keys("standard_user")

            pwd = driver.find_element(By.ID, "password")
            pwd.send_keys("secret_sauce")

            login_btn = driver.find_element(By.ID, "login-button")
            login_btn.click()

            logging.info("User has been logged in successfully")

            # Validate products
            products = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_name"))
            assert len(products) == 6
            logging.info("Products have been validated successfully")

            # Add products into cart
            product_1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
            product_1.click()
            product_2 = wait_for_clickable(driver,(By.ID, "add-to-cart-sauce-labs-bike-light"))
            product_2.click()   
            product_3 = wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
            product_3.click()     

            logging.info("Products have been added into cart successfully")

            # Cart
            cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_btn.click()

            cart_items = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_name"))

            for item in cart_items:
                print(item.text)

            logging.info("Cart has been validated successfully")

            take_screenshot(driver, "e_commerce_automation/screenshots/cart_page_validate.png")

            assert "cart.html" in driver.current_url, "Cart page not loaded"

            # Checkout
            checkout_btn = wait_for_clickable(driver, (By.ID, "checkout"))
            checkout_btn.click()

            fname = driver.find_element(By.ID, "first-name")
            fname.send_keys("siri")

            lname = driver.find_element(By.ID, "last-name")
            lname.send_keys("kuravi")

            pcode = driver.find_element(By.ID, "postal-code")
            pcode.send_keys("516002")

            continue_btn = driver.find_element(By.ID, 'continue')
            continue_btn.click()

            logging.info("Checkout process has been started")

            products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

            prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

            for p, pr in zip(products, prices):
                print(f"{p.text} - {pr.text}")

            driver.find_element(By.ID, "finish").click()

            success_msg = wait_for_visibility(driver, (By.CLASS_NAME, "complete-header"))
            validate_text(success_msg.text, "Thank you for your order!")

            logging.info("Order has been placed successfully")

            take_screenshot(driver, "e_2_e_order")


            # Logout
            menu_btn = wait_for_clickable(driver, (By.CSS_SELECTOR, "#react-burger-menu-btn"))
            menu_btn.click()

            logout_btn = wait_for_clickable(driver, (By.ID, "logout_sidebar_link"))
            logout_btn.click()

            logging.info("Logout successful")

        
        except Exception as e:
            print(e)

    e_2_e_flow()
