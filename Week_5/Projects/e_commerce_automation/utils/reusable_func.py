from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

wait = WebDriverWait(driver, 10)

def wait_for_visibility(driver, locator):
   wait.until(EC.visibility_of_element_located((By.locator)))

def wait_for_clickable(driver, locator):
    e = wait.until(EC.element_to_be_clickable((By.locator)))
    e.click()

def take_screenshot(driver, filename):
    i = 1
    while True:
        if not os.path.isfile(f'./screenshots/{filename}{i}.png'):
            driver.save_screenshot(f'./screenshots/{filename}{i}.png')
            print("Screenshot has been saved successfully")
            break
        i += 1



