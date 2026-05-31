from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")

print(driver.title)
print(driver.current_url)


driver.get("https://github.com")
print(driver.title)

driver.quit()