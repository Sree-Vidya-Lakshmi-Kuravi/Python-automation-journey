from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/webtables?utm_source=chatgpt.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    def find_employee(name):
        rows = driver.find_elements(By.XPATH, '//tbody/tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')

            if cells[0].text == name:
                print("Salary:",cells[4].text)

    emp = find_employee("Cierra")

    if emp:
        print("Employee found")
        print(emp)

        sal = emp["salary"]
        print("Salary:", sal)

        if sal >= 10000:
            print("Salary is greater than 10000")

        else:
            print("Salary is not greater than 10000")
        
    else:
        print("Employee not found")