from selenium.webdriver.common.by import By
import time
from .data import store_metadata, get_post_metadata

def like_posts(driver, num_posts):
    driver.get("https://www.instagram.com/explore/")
    time.sleep(3)

    first_post = driver.find_element(By.XPATH, "//article[@role='presentation']//a")
    first_post.click()
    time.sleep(3)

    metadata = []

    for _ in range(num_posts):
        like_button = driver.find_element(By.XPATH, "//section/span/button")
        like_button.click()
        time.sleep(2)

        metadata.append(get_post_metadata(driver))

        next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
        next_button.click()
        time.sleep(2)

    store_metadata(metadata)
