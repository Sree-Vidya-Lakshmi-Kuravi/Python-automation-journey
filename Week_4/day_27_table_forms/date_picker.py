from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

with webdriver.Chrome() as driver:

    driver.get("https://demoqa.com/date-picker?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 10)

    date_textbox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#datePickerMonthYearInput")))
    time.sleep(2)

    date_textbox.send_keys(Keys.CONTROL + "a")
    date_textbox.send_keys(Keys.DELETE)

    # Printing today's date
    today = date.today().strftime("%m/%d/%Y")
    print("Today's date:", today)
    date_textbox.send_keys(today)


    # Printing custom date
    custom_date = "12/23/2004"
    date_textbox.send_keys(Keys.CONTROL + "a")
    date_textbox.send_keys(Keys.DELETE)
    date_textbox.send_keys(custom_date)
    print("Selected date:", custom_date)

    driver.save_screenshot('./screenshots/date_picker.png')

    # Validating selected date
    sel_date = date_textbox.get_attribute("value")
    if sel_date == custom_date:
        print("Validation successful")
    else:
        print("Validation failed")