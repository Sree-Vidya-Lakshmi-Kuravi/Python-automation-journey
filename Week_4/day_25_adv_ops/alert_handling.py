
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # explicit wait
from selenium.webdriver.support import expected_conditions as EC  # expected conditions
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as driver:  # automatically closes o need of driver.quit()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 10)

    # Finding the alert
    normal_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")))
    normal_alert.click()

    # Handling the normal alert (Contains only OK button)
    driver.switch_to.alert.accept()
    res = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="result"]')))
    print(res.text)


    # Handling the JS  alert (contains OK and Cancel buttons)
    js_alert = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")))
    js_alert.click()

    driver.switch_to.alert.accept()
    res2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="result"]')))
    print(res2.text)
    

    # Handling JS Prompt (sending the user input and then clicking on OK)
    js_prompt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button")))
    js_prompt.click()

    driver.switch_to.alert.send_keys("Hoyna Hoyna")
    driver.switch_to.alert.accept()
    res3 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="result"]')))
    print(res3.text)
