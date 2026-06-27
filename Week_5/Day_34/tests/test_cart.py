import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(login_fixture):
    wait = WebDriverWait(login_fixture, 10)
    product = login_fixture.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    product.click()

    cart_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#shopping_cart_container > a > span")))

    assert cart_btn.text == '1', "Cart products length mismatched"
    print("Product added to cart successfully")


def test_remove_from_cart(login_fixture):
    wait = WebDriverWait(login_fixture, 10)
    product = login_fixture.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    product.click() 

    rm_product = login_fixture.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
    rm_product.click()

    cart_btn = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    cart_items = login_fixture.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_items) == 0, "Cart should be empty after removal"
    print("✅ Product removed from cart successfully")
