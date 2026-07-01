import pytest
from selenium.webdriver.common.by import By

def test_checkout(login_fixture_for_all):
    # Add product to cart
    product = login_fixture_for_all.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    product.click()

    # Cart badge 
    cart_badge = login_fixture_for_all.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == '1', "Cart count mismatched"
    print("Cart validated")

    # Go to cart page
    login_fixture_for_all.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in login_fixture_for_all.current_url, "Wrong page"
    print("Cart page displayed")

    # checkout
    login_fixture_for_all.find_element(By.ID, "checkout").click()
    assert "checkout-step-one" in login_fixture_for_all.current_url, "Checkout page not displayed"
    print("Checkout page displayed")

    # Fill user details
    login_fixture_for_all.find_element(By.ID, "first-name").send_keys("siri")
    login_fixture_for_all.find_element(By.ID, "last-name").send_keys("kuravi")
    login_fixture_for_all.find_element(By.ID, "postal-code").send_keys("Planet earth")

    # checkout
    login_fixture_for_all.find_element(By.ID, "continue").click()
    print(login_fixture_for_all.current_url)
    assert 'checkout-step-two' in login_fixture_for_all.current_url, "Not loaded second page"
    print("User details entered correctly for checkout")

    # # finish
    # login_fixture_for_all.find_element(By.ID, "finish").click()
    # verify_text = login_fixture_for_all.find_element(By.CSS_SELECTOR, "#checkout_complete_container > h2")
    # print(verify_text.text)
