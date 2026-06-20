from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.reusable_func import *
from login_tests import *

### Product Inventory Validation

with webdriver.Chrome() as driver:

    driver.get("https://www.saucedemo.com/")

    def product_count():
        login(driver, "standard_user", "secret_sauce")
        products = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item"))
        print("Number of products:", len(products))

        assert len(products) == 6, f"Expected number of products is 6, found {len(products)}"
        print("Product count is validated")
    
    # product_count()

    def product_names():
        product_count()
        names = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_name"))
        print("The names of the products:")
        for name in names:
            print(name.text)
        return names

    # product_names()

    def product_prices():
        # product_count()
        prices = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_price"))
        print("The prices of the products:")
        for price in prices:
            print(price.text)
        return prices
        
    # product_prices()

    def product_info():
        n = product_names()
        p = product_prices()

        names = [name.text for name in n]
        prices = [price.text for price in p]

        info = dict(zip(names, prices))
        print(info)

    # product_info()