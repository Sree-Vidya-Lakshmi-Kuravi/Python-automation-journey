from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/webtables?utm_source=chatgpt.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    def add_emp(fname, lname, email, age, salary, dept):
        # Click Add button first
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_btn.click()

        wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(fname)
        driver.find_element(By.ID, "lastName").send_keys(lname)
        driver.find_element(By.ID, "userEmail").send_keys(email)
        driver.find_element(By.ID, "age").send_keys(str(age))
        driver.find_element(By.ID, "salary").send_keys(str(salary))
        driver.find_element(By.ID, "department").send_keys(dept)

        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_btn.click()

        driver.save_screenshot('./day_27_emp_mgmt_validation/screenshots/add_employee.png')

        print(f"Employee {fname} {lname} added successfully.")

        time.sleep(2)
    


    def search_emp(name):
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "searchBox")))
        search_box.click()
        time.sleep(2)
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(1)

        driver.save_screenshot('./day_27_emp_mgmt_validation/screenshots/search_employee.png')


        rows = driver.find_elements(By.CSS_SELECTOR, "#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 > div.container-fluid > div.web-tables-wrapper > table > tbody")

        if rows and name in rows[0].text:
            print(f"Employee {name} found.")
            return True
        else:
            print(f"Employee {name} not found.")
            return False


    def edit_emp(name, new_email):
        if search_emp(name):
            edit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Edit']")))
            edit_btn.click()

            email = driver.find_element(By.ID, "userEmail")
            email.clear()

            email.send_keys(new_email)
            time.sleep(2)

            driver.find_element(By.ID, "submit").click()

            driver.save_screenshot('./day_27_emp_mgmt_validation/screenshots/edit_employee.png')


            print(f"Employee {name} email updated to {new_email}.")
        else:
            print("Employee not found")

    
    def del_emp(name):
        if search_emp(name):
            del_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title = 'Delete']")))
            del_btn.click()
            time.sleep(2)

            driver.save_screenshot('./day_27_emp_mgmt_validation/screenshots/add_employee.png')

            print(f"Employee {name} has been deletd successfully")

        else:
            print("No such employee found")

        
    add_emp("BVNS", "Kuravi", "bvns@gmail.com", 21, 450000, "Rocket Science")
    search_emp("BVNS")
    edit_emp("BVNS", "bvns45@gmail.com")
    del_emp("Cierra")

