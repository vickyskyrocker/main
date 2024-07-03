import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
wait = WebDriverWait(driver, 10000)
wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class = 'active']")))
elementToClick = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-danger')]")
print("element to click text is " + elementToClick.text)
elementToClick.click()
time.sleep(5)
handleAlert = driver.switch_to.alert
handleAlert.accept()
time.sleep(5)
