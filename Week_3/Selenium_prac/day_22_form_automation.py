## Form Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")

driver.maximize_window()

print("Title:", driver.title)

# Full name
full_name = driver.find_element(By.ID, "userName").send_keys("Hela")
time.sleep(1)

email = driver.find_element(By.ID, "userEmail").send_keys("yelahelahela@gmail.com")
time.sleep(1)

c_add = driver.find_element(By.ID, "currentAddress").send_keys("Nethaji puttina chota geethanjali paadina chota")
time.sleep(1)

p_add = driver.find_element(By.ID, "permanentAddress").send_keys("Nethaji puttina chota geethanjali paadina chota")
time.sleep(1)

# scrolling the page
driver.execute_script('window.scrollTo(0, 600);')

driver.find_element(By.ID, "submit").click()
time.sleep(2)

output = driver.find_element(By.ID, "output")
print(output.text)

