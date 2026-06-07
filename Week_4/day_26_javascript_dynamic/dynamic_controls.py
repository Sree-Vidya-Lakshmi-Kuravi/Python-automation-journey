from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/automation-practice-form?utm_source=chatgpt.com")
    print("Title:", driver.title)

    wait = WebDriverWait(driver, 10)

    # title using js
    page_title = driver.execute_script("return document.title;")
    print("Page title using javascript:", page_title)
    
    # clicking button using js
    submit_btn = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
    driver.execute_script("arguments[0].click();", submit_btn)
    time.sleep(2)

    # highlighting an element
    form_style = wait.until(EC.visibility_of_element_located((By.ID, "userForm")))
    time.sleep(2)
    driver.execute_script("arguments[0].style.border = '3px solid red'", form_style)
    time.sleep(3)
    driver.execute_script("arguments[0].style.backgroundColor = 'green';", form_style)
    time.sleep(2)

    # scrolling
    # scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # scroll to top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # scroll to submit button
    driver.execute_script("arguments[0].scrollIntoView()", submit_btn)
    time.sleep(2)

    driver.get("https://the-internet.herokuapp.com/dynamic_controls?utm_source=chatgpt.com")
    print("Title:", driver.title)

    wait = WebDriverWait(driver, 20)

    cb_remove = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
    cb_remove.click()
    time.sleep(2)

    cb_msg = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
    print(cb_msg.text)

    cb_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
    cb_add.click()
    time.sleep(2)

    cb_msg = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
    print(cb_msg.text)

    enable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
    enable_btn.click()
    time.sleep(2)

    enable_btn_msg = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
    print(enable_btn_msg.text)
    time.sleep(2)

    driver.get("https://testautomationpractice.blogspot.com/")
    print("Title:", driver.title)

    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    name = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@id, "name")]')))
    name.send_keys("BVNS")
    time.sleep(2)

    email = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[starts-with(@id, "email")]')))
    email.send_keys("bvns@gmail.com")
    time.sleep(2)

    ph = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@id, "phone")]')))
    ph.send_keys("899898998989")
    time.sleep(2)

    driver.save_screenshot('./screenshots/dynamic_controls.png')

    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)

    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Submit"]')))
    submit_btn.click()
    time.sleep(2)