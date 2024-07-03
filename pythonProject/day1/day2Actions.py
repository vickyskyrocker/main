import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
wait = WebDriverWait(driver, 10000)
wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
actions = ActionChains(driver)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'draggable']")))
sourceEle = driver.find_element(By.XPATH, "//div[@id = 'draggable']")
targetEle = driver.find_element(By.XPATH, "//div[@id = 'droppable']")
actions.drag_and_drop(sourceEle, targetEle).perform()
time.sleep(5)
print("Image is dropped")











