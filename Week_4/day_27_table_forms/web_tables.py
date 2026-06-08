from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/webtables?utm_source=chatgpt.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    tables = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'table')))
    time.sleep(2)

    # # printing all rows in a table
    for i in tables:
        print(i.text)

    # # Print first name, last name, email
    rows = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//tbody/tr')))

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        print(f"First Name: {cells[0].text},"
        f"Last Name: {cells[1].text},"
        f"Email: {cells[3].text}")

    # counting total rows
    print("Number of rows:", len(rows))

    # # counting columns
    cols = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//thead/tr/th')))

    # for col in cols:
    #     print(col.text)

    print("Number of columns:", len(cols))

    # # Search for Cierra
    search_box = wait.until(EC.visibility_of_element_located((By.ID, 'searchBox')))
    search_box.send_keys("Cierra")

    time.sleep(2)

    results = driver.find_elements(By.XPATH,
    "//tbody/tr/td[text()='Cierra']")

if len(results) > 0:
    print("Cierra exists")
else:
    print("Cierra not found")
    
