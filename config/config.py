import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVER_PATH = os.path.join(BASE_DIR, 'drivers', 'geckodriver')  # Adjust if using another driver
INSTAGRAM_URL = "https://www.instagram.com"
LOGIN_URL = f"{INSTAGRAM_URL}/accounts/login/"
USERNAME = "your_username"
PASSWORD = "your_password"
