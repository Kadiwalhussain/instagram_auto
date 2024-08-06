from scripts.login.py import login_instagram
from scripts.actions import like_posts

def main():
    driver = login_instagram()
    like_posts(driver, 10)
    driver.quit()

if __name__ == "__main__":
    main()
