
from selenium import webdriver
from selenium.webdriver.common.by import By  # import statement for locators
from selenium.webdriver.support.ui import WebDriverWait  # explicit wait
from selenium.webdriver.support import expected_conditions as EC  # expected conditions

driver = webdriver.Chrome()

# --- IMPLICIT WAIT ---
driver.implicitly_wait(10) # global i.e., it is for all elements. Waits until element is found and stops early if the element is found

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tom")

# clear - to clear the data
driver.find_element(By.XPATH, '//*[@id="username"]').clear()

username = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")

password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")


### ---  EXPLICIT WAIT  ---

driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")

wait = WebDriverWait(driver, 60)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button")))

login.click()

msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

print(msg.text)


driver.get("https://the-internet.herokuapp.com/dynamic_loading/1?utm_source=chatgpt.com")
print("Title:", driver.title)

driver.find_element(By.CSS_SELECTOR, "#start > button").click()

# visibility_of_element_located - if the condition is visible to user and should be in the HTML code
msg = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(msg.text)

# presence_of_element_located = should be in the HTML code
msg1 = wait.until(EC.presence_of_element_located((By.ID, "finish")))
print(msg1.text)

driver.quit()