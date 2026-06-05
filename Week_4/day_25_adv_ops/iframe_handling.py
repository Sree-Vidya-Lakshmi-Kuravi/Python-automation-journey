from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as driver:
    
    ## IFRAME HANDLING
    # Open the browser
    # Locate the iframe
    # Perform operations
    # Close the iframe
    # Perform operations for the content outside the iframe
    driver.get("https://demo.automationtesting.in/Frames.html")

    wait = WebDriverWait(driver, 60)

    i_frame = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="singleframe"]')))
    driver.switch_to.frame(i_frame)

    # Entered into the iframe
    demo_text = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/h5')))
    print(demo_text.text)

    texting = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div/input')))
    texting.clear() # clearing the present content

    texting.send_keys("La la la la")
    driver.implicitly_wait(2)

    driver.switch_to.default_content()  # comes back to the page from iframe content page

    i_within = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a"))).click()
    time.sleep(2)
    
    outer = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/iframe")))
    driver.switch_to.frame(outer)

    inner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div')))
    driver.switch_to.frame(inner)
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div/input"))).send_keys("Hii raa ")

    time.sleep(3)

    
