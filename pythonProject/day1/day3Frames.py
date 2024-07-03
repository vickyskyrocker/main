import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()
wait = WebDriverWait(driver, 10000)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "frame")))
elementToClick = driver.find_element(By.XPATH, "//input[@type = 'text']")
elementToClick.send_keys("42987676567")
time.sleep(10)
print("element is entered")





