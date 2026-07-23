import pytest
from pages.login_page import *
from pages.inventory_page import *
from config.config_reader import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_successful_login(browser_fixture):
    """Verifies successful login"""
    # Step 1: Login
    log_page = LoginPage(browser_fixture)
    log_page.login(ConfigReader.get_username("standard_user"), ConfigReader.get_password())

    # Step 2: Verifies the inventory page loaded
    inv_page = InventoryPage(browser_fixture)
    assert inv_page.is_inventory_loaded() is True, "Unable to load the inventory page"
    assert inv_page.get_product_count() == 6, "Products mismatched"

@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
def test_locked_user(browser_fixture):
    """Negative login"""
    # Step 1: Login
    log_page = LoginPage(browser_fixture)
    log_page.login(ConfigReader.get_username("locked_out_user"), ConfigReader.get_password())

    # Step 2: Returns the error message
    msg = log_page.get_error_msg()
    assert "Epic sadface: Sorry, this user has been locked out." in msg, "No error msg"
