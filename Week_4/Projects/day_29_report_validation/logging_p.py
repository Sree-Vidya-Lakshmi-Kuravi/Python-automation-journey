import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Minimum level to capture
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("selenium_log.log"),  # Save logs to file
        logging.StreamHandler()                   # Show logs in console
    ])


def validate_msg(output_text):
    text = output_text.strip().lower()
    if "invalid" in text:
        return "failed"
    elif "secure area" in text:
        return "success"
    else:
        return "unknown"

try:
    with webdriver.Chrome() as driver:
        driver.get("https://the-internet.herokuapp.com/login?utm_source=chatgpt.com")
        logging.info("Browser launched")

        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username.send_keys("tomsmith")
        logging.debug("Username entered successfully")

        time.sleep(2)

        pwd = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        pwd.send_keys("SuperSecretPassword!")
        logging.debug("Entered password")

        time.sleep(2)

        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button")))
        login_btn.click()
        logging.info("Submitted the data")
        time.sleep(2)

        output = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

        print("Output:", output.text)

        result = validate_msg(output_text)

        if result == "failed":
            logging.info("Login failed")
            driver.save_screenshot('./screenshots/login_failed.png')

        elif result == "success":
            logging.info("Login success")
            driver.save_screenshot('.screenshots/login_success.png')

        else:
            logging.warning("Something went wrong")

except Exception as e:
    logging.error("Test failure occurred due to: %s", e)
