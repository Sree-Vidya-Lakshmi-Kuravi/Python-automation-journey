## Pytest implementation

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title, "Google not found in the title"
    print("Google is present in title")
    driver.quit()
# test_google()

def test_saucedemo_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url, "Unable to login"
    print("Login success")

# test_saucedemo_login()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user1")
    driver.find_element(By.ID, "password").send_keys("secret_sauce1")
    driver.find_element(By.ID, "login-button").click()

    msg = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    print(msg.text)

    assert "do not match" in msg.text, "Login success"
    print("Invalid credentials")

# test_invalid_login()


def test_product_count():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()    
  
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6, f"Expected 6 products, found {len(products)}"
    print(f"The total length of products: {len(products)}")

# test_product_count()


# To run these functions all at a time => pytest
# Example:
# ============= test session starts ==============
# platform win32 -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
# rootdir: E:\Vidya Career\IT JOB\Repati Kosam\Week_5\Day_33
# collected 4 items                               

# test_google.py ....                       [100%]

# ============== 4 passed in 9.96s ===============


# To run all these functions at a time, but it would test each file at a time => pytest -v
# Example:
# ============= test session starts ==============
# platform win32 -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0 -- E:\Vidya Career\IT JOB\Repati Kosam\rkvenv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: E:\Vidya Career\IT JOB\Repati Kosam\Week_5\Day_33
# collected 4 items                               

# test_google.py::test_google PASSED        [ 25%]
# test_google.py::test_saucedemo_login PASSED [ 50%]
# test_google.py::test_invalid_login PASSED [ 75%]
# test_google.py::test_product_count PASSED [100%]

# ============== 4 passed in 11.60s ==============


# To print the print() messages => pytest -v -s
# Example:
# ============= test session starts ==============
# platform win32 -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0 -- E:\Vidya Career\IT JOB\Repati Kosam\rkvenv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: E:\Vidya Career\IT JOB\Repati Kosam\Week_5\Day_33
# collected 4 items                               

# test_google.py::test_google Google is present in title
# PASSED
# test_google.py::test_saucedemo_login Login success
# PASSED
# test_google.py::test_invalid_login Epic sadface: Username and password do not match any user in this service
# Invalid credentials
# PASSED
# test_google.py::test_product_count The total length of products: 6
# PASSED

# ============== 4 passed in 12.01s ==============
