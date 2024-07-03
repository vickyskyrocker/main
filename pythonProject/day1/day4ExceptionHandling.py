import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://demoqa.com/select-menu")
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.XPATH, "//h2").click()
    print("try block is executed")

except NoSuchElementException as e:
    print(f"element not found exception : {e}")

finally:
    print("finally block is executed")
    driver.quit()
