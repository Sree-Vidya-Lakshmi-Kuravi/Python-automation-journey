import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.regression
def test_checkout(login_fixture_for_all):
    driver = login_fixture_for_all
    wait = WebDriverWait(driver, 30)

    # Add product to cart
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
    add_to_cart.click()

    # Validate cart badge
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1", "Cart count mismatched"
    print("Cart validated")

    # Go to cart page
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    wait.until(EC.url_contains("cart.html"))
    assert "cart.html" in driver.current_url, "Wrong page"
    print("Cart page displayed")

    # Checkout page
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    wait.until(EC.url_contains("checkout-step-one"))
    assert "checkout-step-one" in driver.current_url, "Checkout page not displayed"
    print("Checkout page displayed")

    # Fill user details
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Loki")
    driver.find_element(By.ID, "last-name").send_keys("Asgardian")
    driver.find_element(By.ID, "postal-code").send_keys("522001")

    print("Details entered")

    # Continue
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_btn.click()

    errors = driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")

    if errors:
        print("Error:", errors[0].text)
    else:
        print("No error message")

    # Wait for Step Two
    wait.until(EC.url_contains("checkout-step-two"))

    assert "checkout-step-two" in driver.current_url, "Checkout Step Two not loaded"
    print("Checkout Step Two loaded successfully")

    # Finish Order
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()

    # Validate Success Page
    success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))

    assert success_msg.text == "Thank you for your order!", "Order completion failed"

    print(success_msg.text)
    print("Checkout completed successfully.")