from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

DEFAULT_TIMEOUT = 10  # time in seconds for waits

# checks whether element is visible
def wait_for_visibility(driver, element, t = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    return wait.until(EC.visibility_of_element_located((element)))

# checks whether element is clickable
def wait_for_clickable(driver, element, t = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    return wait.until(EC.element_to_be_clickable((element)))

# checks whether element is present only in HTML structure
def wait_for_presence(driver, element, t = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    return wait.until(EC.presence_of_element_located((element)))

# checks whether multiple elements are found
def wait_for_visibility_all(driver, element, t = DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, t)
    return wait.until(EC.visibility_of_all_elements_located((element)))
