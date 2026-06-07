from selenium import webdriver
from selenium.webdriver.common.by import By

import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/automation-practice-form?utm_source=chatgpt.com")

    print("Title:", driver.title)

    driver.maximize_window()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    sub = driver.find_element(By.ID, 'submit')

    driver.execute_script('arguments[0].click()', sub)

    driver.save_screenshot('./screenshots/scrolling.png')