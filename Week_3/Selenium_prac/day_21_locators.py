
from selenium import webdriver
from selenium .webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")


driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
time.sleep(2)


driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
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