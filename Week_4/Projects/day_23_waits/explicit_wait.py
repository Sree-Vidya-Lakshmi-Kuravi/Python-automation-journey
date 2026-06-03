### DYNAMIC LOGIN AUTOMATION

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.utils import validate

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")
print("Title:", driver.title)

wait = WebDriverWait(driver, 60)

name = wait.until(EC.visibility_of_element_located((By.ID, "username")))
name.send_keys("tomsmith")

p = wait.until(EC.visibility_of_element_located((By.ID, "password")))
p.send_keys("SuperSecretPassword!")

login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button")))
login.click()

m = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
print(m.text)

validate(m.text, "You logged into a secure area!")

driver.quit()