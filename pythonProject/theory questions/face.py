import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_val_login(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("ramyamam93@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("ramya93@Mam")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)


def test_inva_login(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("ramyamam93@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("password")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)
def test_inuser_login(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("ramya93@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("password")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)
def test_inpass_login(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("ramyamam93@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("password")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

def test_mt_cre(setup):
    driver = setup
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)







