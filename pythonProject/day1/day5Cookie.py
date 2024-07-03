import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
time.sleep(10)
beforeAdding = driver.get_cookies()
for cookie in beforeAdding:
    print(f"before adding the cookie : {cookie}")

addCookie = {'name': 'vignesh', 'value': '76547723'}
driver.add_cookie(addCookie)
getCookies = driver.get_cookies()
for cookie in getCookies:
    print(f"after adding the cookie : {cookie}")

time.sleep(10)

myCookie = driver.get_cookie('vignesh')
print(myCookie)

deleteCookie = driver.delete_cookie('vignesh')

updatedCookie = driver.get_cookies()
for cookie in updatedCookie:
    print(f"after deleting the cookie : {cookie}")

time.sleep(10)


