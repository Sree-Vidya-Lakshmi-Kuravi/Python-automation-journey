from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/checkbox?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 10)

    tree = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div/span[2]')))
    tree.click()
    time.sleep(2)

    desktop_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[2]/span[3]')))
    desktop_btn.click()
    time.sleep(2)

    doc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[3]/span[3]')))
    doc_btn.click()
    time.sleep(2)

    msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#result')))
    print(msg.text)

    driver.save_screenshot('./screenshots/checkbox.png')

    if "desktop" in msg.text.lower() or "document" in msg.text.lower():
        print("Desktop and Documents have been selected successfully")
    else:
        print("Not selected")