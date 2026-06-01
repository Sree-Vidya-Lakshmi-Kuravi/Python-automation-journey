from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Google
driver.get("https://google.com")

print(driver.title)
print(driver.current_url)

# Opening Github
driver.get("https://github.com")
print(driver.title)

driver.quit()