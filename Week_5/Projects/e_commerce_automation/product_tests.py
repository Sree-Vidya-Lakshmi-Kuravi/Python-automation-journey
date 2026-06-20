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
    
    product_count()