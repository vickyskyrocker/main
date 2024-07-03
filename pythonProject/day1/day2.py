import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
wait = WebDriverWait(driver, 10000)
wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
dropdown.select_by_visible_text("Yellow")
time.sleep(5)
print("yellow is clicked and printed")









