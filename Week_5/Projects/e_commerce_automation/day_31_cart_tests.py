from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from utils.reusable_func import *
from login_tests import *


with webdriver.Chrome() as driver:
    driver.get("https://www.saucedemo.com/")

## Adding single product to cart
    def add_single_product():
        login(driver, "standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url, "Product page is loaded"

        add_btn = wait_for_clickable(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
        add_btn.click()
        print("Added to cart successfully")

        cart_count = wait_for_visibility(driver, (By.CSS_SELECTOR, "#shopping_cart_container > a > span"))
        assert cart_count.text == "1", f"Expected cart count 1, got {cart_count.text}"
        
        print(cart_count.text)

    # add_single_product()

## Adding multiple products to cart
    def add_mul_products(*locators):
        login(driver, "standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url, "Product page is loaded"

        for locator in locators:
            lctr = wait_for_clickable(driver, locator)
            lctr.click()
            print("Added to cart successfully")
        

        cart_count = wait_for_visibility(driver, (By.CSS_SELECTOR, "#shopping_cart_container > a > span"))
        expected = len(locators)

        # assert cart_count.text == str(expected), f"Expected cart count {expected}, got {cart_count.text}"
        
        print("Cart count validation:", cart_count.text)

    # add_mul_products(
    # (By.ID, "add-to-cart-sauce-labs-bike-light"), 
    # (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"), 
    # (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))


## Product names in cart
    def cart_p_names():
        cart_product_names = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_name"))
        names = [c.text for c in cart_product_names]
        print("Cart product names:", names)
        return names


## Product prices in cart
    def cart_p_prices():
        cart_product_prices = wait_for_visibility_all(driver, (By.CLASS_NAME, "inventory_item_price"))
        prices = [cp.text for cp in cart_product_prices]
        print("Cart product prices:", prices)
        return prices


## Printing the details of products in cart
    def cart_info():
        add_mul_products(
        (By.ID, "add-to-cart-sauce-labs-bike-light"), 
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"), 
        (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))

        cart_btn = wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"))
        cart_btn.click()

        names = cart_p_names()
        prices = cart_p_prices()

        info = dict(zip(names, prices))
        print("Cart Info:", info)
        return info
    
    cart_info()


# --- Helper: get cart count safely ---
    def get_cart_count(driver):
        try:
            cart_count = wait_for_visibility(driver, (By.CSS_SELECTOR, "#shopping_cart_container > a > span"), t=3)
            return int(cart_count.text)
        except TimeoutException:
            return 0

## The product to remove in the cart
    def product_to_remove(driver, product_locator, remove_locator):
        wait_for_visibility(driver, product_locator)
        rem = wait_for_clickable(driver, remove_locator)
        rem.click()
        print("Product removed successfully from cart")

        try:
            WebDriverWait(driver, 4).until(EC.invisibility_of_element_located(product_locator))
            print("Product is no longer in the cart")
        except TimeoutException:
            print("Product is still in the cart")


## Removing the product in the cart
    def remove_cart_product():
        add_mul_products(
            (By.ID, "add-to-cart-sauce-labs-bike-light"),
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        )

        cart_btn = wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"))
        cart_btn.click()

        product_to_remove(driver, (By.ID, "item_1_title_link"), (By.ID, "remove-sauce-labs-bolt-t-shirt"))
        time.sleep(2)

        # -- Check cart status
        count = get_cart_count(driver)
        if count == 0:
            print("No items in the cart")
        else:
            print(f"Cart has {count} item(s) remaining")

    # remove_cart_product()

    take_screenshot(driver, 'cart_page')


##### ---- second way ----
# def remove_product(cart, product_name):
#         """Remove product by name using relative XPath instead of input()."""
#         wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()
#         remove_btn = driver.find_element(
#             By.ID,
#             "remove-"+product_name.lower().replace(' ', '-')
#         )
#         remove_btn.click()
#         print(f"Product '{product_name}' removed successfully")
#         wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link"), 30).click()
#         driver.refresh()
#         cart_validation()
