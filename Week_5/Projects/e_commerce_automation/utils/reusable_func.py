from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

DEFAULT_TIMEOUT = 10  # time in seconds for waits
wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

# checks whether element is visible
def wait_for_visibility(driver, element):
   wait.until(EC.visibility_of_element_located((element)))

# checks whether element is clickable
def wait_for_clickable(driver, element):
    e = wait.until(EC.element_to_be_clickable((element)))

# checks whether element is present only in HTML structure
def wait_for_presence(driver, element):
    e = wait.until(EC.presence_of_element_located((element)))


# Function for screenshot
def take_screenshot(driver, filename):
    i = 1
    while True:
        if not os.path.isfile(f'./screenshots/{filename}{i}.png'):
            driver.save_screenshot(f'./screenshots/{filename}{i}.png')
            print("Screenshot has been saved successfully")
            break
        i += 1


# validating the url
def validate_url(actual, expected):
    if expected not in actual:
        print(f"'{expected}' is not present in url '{actual}'")
        return False
    else:
        print(f"'{expected}' is present in url '{actual}'")
        return True


# validate text
def validate_text(actual, expected):
    if expected in actual:
        print(f"Text has been matched successfully.\n Actual text: {actual}\n Expected Text: {expected}")
        return True
    else:
        print(f"Text has not matched successfully.\n Actual text: {actual}\n Expected Text: {expected}")
        return True



