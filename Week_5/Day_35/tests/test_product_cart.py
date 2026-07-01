import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("product", ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"])

def test_product_in_cart(login_fixture_for_all, product):
    product_list = login_fixture_for_all.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in product_list]
    print(product_names)

    assert product in product_names, "Product not found"
    print(f"Product: {product} found in the cart")

