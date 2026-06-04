### DROPDOWN HANDLING

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/select-menu")
    wait = WebDriverWait(driver, 10) # For explicit wait
    driver.maximize_window()

    # Locating the dropdown
    dropdown = wait.until(EC.visibility_of_element_located((By.ID, "oldSelectMenu")))
    sel = Select(dropdown)

    # select by visible text
    sel.select_by_visible_text("Blue")

    # printing selected option
    selected = sel.first_selected_option
    print(selected.text)

    # select by value
    # sel.select_by_value("4")

    # # select by index
    # sel.select_by_index(2) # 2 means 3rd value


    # all_options = sel.options
    # for option in all_options:
    #     print(option.text)

    #### ---- SELECTING MULTIPLE OPTIONS IN DROPDOWN ----

    mul_sel = wait.until(EC.visibility_of_element_located((By.ID, "cars")))
    Select(mul_sel.select_by_value("volvo"))
    Select(mul_sel.select_by_value("audi"))

    sel_options = Select(mul_sel).all_selected_options
    for option in sel_options:
        print(f"Selected: {option.text}")

    driver.implicitly_wait(6)