import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.regression
@pytest.mark.inventory
def test_inventory_item_count_and_titles(browser_fixture):
    """Verify 6 products are displayed on the inventory page with non-empty names."""
    # Step 1: Login
    login_page = LoginPage(browser_fixture)
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Verify inventory product list
    inventory_page = InventoryPage(browser_fixture)
    assert inventory_page.get_product_count() == 6, "Inventory should display exactly 6 products"

    # Step 3: Verify the product names
    product_names = inventory_page.get_product_names()
    assert len(product_names) == 6, "Product names list count mismatch"
    assert "Sauce Labs Backpack" in product_names, "Expected 'Sauce Labs Backpack' in inventory list"