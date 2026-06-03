from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1?utm_source=chatgpt.com")
print("Title:", driver.title)

wait = WebDriverWait(driver, 60)

driver.find_element(By.CSS_SELECTOR, "#start > button").click()

message = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(message.text)


validate_text(message.text, "Hello World!")

driver.quit()