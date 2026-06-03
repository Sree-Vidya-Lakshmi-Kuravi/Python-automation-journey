from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_visibility(driver, ele):
    wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ele))
    return wait

def wait_for_clickable(driver, ele):
    wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ele))
    return wait

def validate(expected, actual):
    if expected in actual:
        print(f"Expected result:{expected}\nActual result:{actual}\nTest Result: SUCCESS")
    else:
        print(f"Expected result:{expected}\nActual result:{actual}\nTest Result: FAILURE")

