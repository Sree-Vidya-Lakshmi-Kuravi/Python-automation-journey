import pytest
from pages.login_page import *
from pages.inventory_page import *
from pages.cart_page import *
from pages.checkout_page import *
from config.config_reader import ConfigReader

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout(browser_fixture):
    """Login, verifies the inventory, adding the product in the cart, entering the user details and finishing the checkout, displaying the thank you message"""
    # Step 1: Login
    log_page = LoginPage(browser_fixture)
    log_page.login(ConfigReader.get_username(), ConfigReader.get_password())

    # Step 2: Verifies the inventory page
    inv_page = InventoryPage(browser_fixture)
    assert inv_page.is_inventory_loaded() is True, "Unable to load the inventory page"
    assert inv_page.get_product_count() == 6, "Products mismatched"

    # Step 3: Add a product in the cart
    cart_page = CartPage(browser_fixture)
    cart_page.add_product()
    assert cart_page.get_cart_count() == 1, "Product has not been added to the cart"
    cart_page.go_to_cart()

    # Step 4: Enter the customer details and checkout
    checkout_page = CheckoutPage(browser_fixture)
    checkout_page.click_checkout()

    checkout_page.enter_first_name("BVNS")
    checkout_page.enter_last_name("kuravi")
    checkout_page.enter_zip_code("516002")
    checkout_page.continue_checkout()
    
    checkout_page.finish_checkout()
    
    # Step 5: Displays the thank you message
    thank_you_msg = checkout_page.get_thank_you_msg()
    assert thank_you_msg == "Thank you for your order!", f"Expected thank you message, but got: '{thank_you_msg}'" 
