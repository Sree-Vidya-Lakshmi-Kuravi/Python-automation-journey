## Form Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## Values
name = "Hela"
email = "yelahelahela@gmail.com"
c_add = "Nethaji puttina chota geethanjali paadina chota"
p_add = "Nethaji puttina chota geethanjali paadina chota"

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")

driver.maximize_window()

print("Title:", driver.title)

driver.find_element(By.ID, "userName").send_keys(name)
time.sleep(1)

driver.find_element(By.ID, "userEmail").send_keys(email)
time.sleep(1)

driver.find_element(By.ID, "currentAddress").send_keys(c_add)
time.sleep(1)

driver.find_element(By.ID, "permanentAddress").send_keys(p_add)
time.sleep(1)


# scrolling the page
driver.execute_script('window.scrollTo(0, 600);')

driver.find_element(By.ID, "submit").click()
time.sleep(2)


# Full name
full_name = driver.find_element(By.ID, "name")
time.sleep(1)

e = driver.find_element(By.ID, "email")
time.sleep(1)

c = driver.find_element(By.CSS_SELECTOR, "#currentAddress.mb-1")
time.sleep(1)

p = driver.find_element(By.CSS_SELECTOR, "#permanentAddress.mb-1")
time.sleep(1)



## Outputs
print(full_name.text)
print(e.text)
print(c.text)
print(p.text)


# Validation function
def validate(actual, expected):
    if expected.lower() in actual.lower():
        print("PASS")
    else:
        print("FAIL")


validate(full_name.text, name)
validate(e.text, email)
validate(c.text, c_add)
validate(p.text, p_add)

time.sleep(1)
driver.quit()