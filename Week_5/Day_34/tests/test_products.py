import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_products(login_fixture):
    products = login_fixture.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6, f"Expected product length:6, Returned {len(products)}"
    print("Number of products validated")

    pro_list = [p.text for p in products]
    print(pro_list)


def test_product_exists(login_fixture):
    product_names = [p.text for p in login_fixture.find_elements(By.CLASS_NAME, "inventory_item_name")]
    print("Product Names:", product_names)

    assert "Sauce Labs Backpack" in product_names, "Back pack product not found"
    print("Found the product")