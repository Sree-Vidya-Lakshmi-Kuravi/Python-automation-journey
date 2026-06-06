from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/menu?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 60)

    actions = ActionChains(driver)

    hover_1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Main Item 1")))

    hover_2 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Main Item 2")))

    hover_2_1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sub Item")))

    hover_2_2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#nav > li:nth-child(2) > ul > li:nth-child(2) > a')))

    hover_2_3 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "SUB SUB LIST »")))

    hover_2_3_1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sub Sub Item 1")))

    hover_2_3_2 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sub Sub Item 2")))

    hover_3 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Main Item 3")))

    actions.move_to_element(hover_1).perform()
    actions.move_to_element(hover_2).perform()
    actions.move_to_element(hover_3).perform()

    time.sleep(2)

    actions.move_to_element(hover_1).perform()
    actions.move_to_element(hover_2).perform()
    actions.move_to_element(hover_2_1).perform()
    actions.move_to_element(hover_2_2).perform()
    actions.move_to_element(hover_2_3).perform()
    actions.move_to_element(hover_2_3_1).perform()
    actions.move_to_element(hover_2_3_2).perform()
    actions.move_to_element(hover_3).perform()

    time.sleep(2)

    driver.save_screenshot('./screenshots/menu_hover.png')
 