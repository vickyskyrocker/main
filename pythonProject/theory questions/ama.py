#Use xpath and automate the below:
   # a.1> Go to amazon --> click on search box --> type iphone
# --> find the element in the result.
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.order(1)
def test_goo_login(setup):
    driver = setup
    driver.get("https://www.google.co.in")
    s_box=driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
    s_box.send_keys("amazon.in")
    s_box.submit()
    amazon_page = driver.find_element(By.XPATH, "(//h3[@class='LC20lb MBeuO DKV0Md'])[1]")
    amazon_page.click()
    a_search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    a_search_box.send_keys("iphone")
    a_search_box.submit()
    pink_iphone = driver.find_element(By.XPATH, "//span[contains(text(),'Apple iPhone 13 (128GB) - Pink')]")
    pink_iphone.click()