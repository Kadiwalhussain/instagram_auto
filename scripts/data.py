import csv
from selenium.webdriver.common.by import By

def store_metadata(metadata):
    with open('metadata.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Profile", "Likes", "Comments", "Date Posted", "Post URL"])
        writer.writerows(metadata)

def get_post_metadata(driver):
    profile_name = driver.find_element(By.XPATH, "//a[@class='FPmhX notranslate nJAzx']").text
    likes = driver.find_element(By.XPATH, "//section//a//span").text
    comments = driver.find_element(By.XPATH, "//ul[@class='XQXOT']//span").text
    date_posted = driver.find_element(By.XPATH, "//time").get_attribute("datetime")
    post_url = driver.current_url

    return profile_name, likes, comments, date_posted, post_url
