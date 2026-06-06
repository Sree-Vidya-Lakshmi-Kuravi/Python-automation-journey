from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/buttons?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 60)

    # Double Click
    d_click = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
    time.sleep(1)
    ActionChains(driver).double_click(d_click).perform()
    time.sleep(3)

    # Right click
    r_click = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
    time.sleep(1)
    ActionChains(driver).context_click(r_click).perform()
    time.sleep(3)

    # Dynamic click
    dynamic_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Click Me"]')))
    time.sleep(1)
    ActionChains(driver).click(dynamic_click).perform()
    time.sleep(3)

    driver.save_screenshot('./screenshots/actions.png')

    