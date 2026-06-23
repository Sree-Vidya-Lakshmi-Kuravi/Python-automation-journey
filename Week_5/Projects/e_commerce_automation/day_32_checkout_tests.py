from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from utils.reusable_func import *
from day_30_login_tests import *

with webdriver.Chrome() as driver:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    def checkout_page():
        try:
            login(driver, "standard_user", "secret_sauce")

            # adding product to cart
            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

            # Clicking cart
            cart_btn = wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"))
            cart_btn.click()

            time.sleep(1)

            # Checkout button
            checkout_btn = driver.find_element(By.ID, "checkout")
            checkout_btn.click()
            
            validate_url(driver.current_url, "checkout-step-one.html")

            time.sleep(1)

            fname = driver.find_element(By.ID, "first-name")
            fname.send_keys("siri")

            lname = driver.find_element(By.ID, "last-name")
            lname.send_keys("kuravi")

            pcode = driver.find_element(By.ID, "postal-code")
            pcode.send_keys("516002")

            continue_btn = driver.find_element(By.ID, 'continue')
            continue_btn.click()

            products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            for p, pr in zip(products, prices):
                print(f"{p.text} - {pr.text}")

            driver.find_element(By.ID, "finish").click()

            success_msg = wait_for_visibility(driver, (By.CLASS_NAME, "complete-header"))
            validate_text(success_msg.text, "Thank you for your order!")

            take_screenshot(driver, "order_success")

        except Exception as e:
            print(e)
        finally:
            driver.quit()


    checkout_page()
