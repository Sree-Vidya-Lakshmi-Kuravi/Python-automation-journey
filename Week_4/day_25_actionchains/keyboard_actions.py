from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/text-box?utm_source=chatgpt.com")

    wait = WebDriverWait(driver, 60)

    username = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    username.send_keys("BVNS")
    time.sleep(2)

    actions = ActionChains(driver)

    actions.send_keys(Keys.TAB).send_keys("bvns@gmail.com").send_keys(Keys.TAB).send_keys("Mars").send_keys(Keys.TAB).send_keys("Mars").perform()
    time.sleep(3)

    actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    time.sleep(2)

    driver.save_screenshot('./screenshots/tab_and_enter.png')
    




