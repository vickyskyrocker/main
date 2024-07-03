from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10000)
username = driver.find_element(By.XPATH, "//input[contains(@name, 'username')]")
username.send_keys("Admin")
password = driver.find_element(By.XPATH, "//input[contains(@name, 'password')]")
password.send_keys("admin123")
loginBtn = driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
loginBtn.click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("login successful")
else:
    print("login failed")









