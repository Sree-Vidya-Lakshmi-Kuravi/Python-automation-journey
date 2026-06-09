from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as driver:

    driver.get("https://demoqa.com/radio-button?utm_source=chatgpt.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    ## Radio Buttons
    yes_btn = wait.until(EC.element_to_be_clickable((By.ID, "yesRadio")))
    yes_btn.click()
    time.sleep(2)

    impress_btn = wait.until(EC.element_to_be_clickable((By.ID, "impressiveRadio")))
    impress_btn.click()
    time.sleep(2)

    msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "text-success")))
    print(msg.text)

    driver.save_screenshot('./screenshots/radio_btn.png')
    
    if "Yes" in msg.text or "Impressive" in msg.text:
        print("Option is validated")
    else:
        print("No such option selected")