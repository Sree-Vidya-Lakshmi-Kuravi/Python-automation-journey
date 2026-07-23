import pytest
from pages.login_page import *
from pages.cart_page import *
from config.config_reader import ConfigReader

@pytest.mark.smoke
@pytest.mark.regression
def cart_test(browser_fixture):
    """Adding and removing the products from the cart"""
    # Step 1: Login
    log_page = LoginPage(browser_fixture)
    log_page.login(ConfigReader.get_username(), ConfigReader.get_password())
    
    cart_page = CartPage(driver)

    # Step 2: Add product in cart
    cart_page.add_product()
    assert cart_page.get_cart_count() == 1, "Cart count should be 1 after adding a product"

    # Step 3: Remove product from cart
    cart_page.remove_product()
    assert cart_page.get_cart_count() == 0, "Cart count should be 0 after removing the product"
