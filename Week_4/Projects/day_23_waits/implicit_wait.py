from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.waits import validate

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://the-internet.herokuapp.com/login')
print("Title:", driver.title)

uname = driver.find_element(By.ID, "username").send_keys("tomsmith")

pwd = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "#login > button").click()

msg = driver.find_element(By.ID, "flash")
print("Text of the msg:", msg.text)

validate(msg.text, "You logged into a secure area!")
driver.quit()