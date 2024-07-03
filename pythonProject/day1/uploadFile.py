import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(10)
file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "file-upload"))
        )
filePath = "E:/Selenium Handbook/testupload.txt"
file_input.send_keys(filePath)
upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "file-submit"))
        )
upload_button.click()
time.sleep(5)
success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']"))
        )
if success_message.is_displayed():
    print(f"File '{filePath}' uploaded successfully.")
else:
    print(f"File '{filePath}' upload failed.")



