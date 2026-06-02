
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")


username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tom")
time.sleep(2)

# clear - to clear the data
driver.find_element(By.XPATH, '//*[@id="username"]').clear()
time.sleep(2)

username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
time.sleep(2)

password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")


# get_attribute() - to find the value based on the attribute
password = driver.find_element(By.XPATH, '//*[@id="password"]')

print(password.get_attribute("id"))  # id - attribute

time.sleep(2)


driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
time.sleep(3)

print(driver.title)
print(driver.current_url)

d = driver.find_element(By.ID, 'flash')
print(d.text)

if "logged in" in d.text:
    print("Login successful")
    logout_b = driver.find_element(By.CSS_SELECTOR, '#content > div > a > i')

    if "Logout" in logout_b.text:
        print("Logout success")
    else:
        print("Logout failed")

else:
    print("Login failed")

driver.quit()