from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=chrome_options)
driver.get("https://facebook.com")
time.sleep(5)
title = driver.title
print(title)
username = driver.find_element(By.ID, "email")
username.send_keys("Email")
print(f"usernameText is entered")
password = driver.find_element(By.ID, "pass")
password.send_keys("Password")
print(f"passwordText is entered")
time.sleep(3)

