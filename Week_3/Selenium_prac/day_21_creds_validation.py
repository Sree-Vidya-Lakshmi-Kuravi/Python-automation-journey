from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
print("Title:", driver.title)
print("URL:", driver.current_url)

driver.find_element(By.NAME, 'username').send_keys("jerry")
driver.find_element(By.CSS_SELECTOR, '#password').send_keys("password")
time.sleep(3)

driver.find_element(By.CLASS_NAME, 'radius').click()

msg = driver.find_element(By.ID, 'flash').text

if 'Your username is invalid' in msg:
    print("Login failed. Enter correct username")

elif 'Your password is invalid' in msg:
    print("Login failed. Enter correct password")

else:
    print("Login successful !!!")


driver.quit()