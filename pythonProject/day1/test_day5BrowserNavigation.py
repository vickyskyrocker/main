import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.co.in")
time.sleep(5)
# Navigates back to demo URL
driver.back()
time.sleep(5)
# Navigates forward to google url
driver.forward()
time.sleep(5)
# refreshes the URl
driver.refresh()
print(driver.current_url)
print("Driver is refreshed")
time.sleep(5)

