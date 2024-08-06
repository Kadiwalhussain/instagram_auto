from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
from config.config import LOGIN_URL, USERNAME, PASSWORD, DRIVER_PATH

def login_instagram():
    options = Options()
    options.headless = False  # Set to True if you want to run in headless mode
    driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
    driver.get(LOGIN_URL)
    time.sleep(3)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

    return driver
