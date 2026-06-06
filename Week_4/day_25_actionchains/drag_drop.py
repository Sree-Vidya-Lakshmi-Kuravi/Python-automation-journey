from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

with webdriver.Chrome() as driver:
    driver.get("https://the-internet.herokuapp.com/drag_and_drop?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 60)

    source = wait.until(EC.visibility_of_element_located((By.ID, "column-a")))

    target = wait.until(EC.visibility_of_element_located((By.ID, "column-b")))

    ActionChains(driver).drag_and_drop(source, target).perform()

    driver.save_screenshot('./screenshots/drag_and_drop.png')
    