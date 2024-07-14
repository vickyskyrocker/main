import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException


# Fixture for setting up the browser
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_book_ticket(setup):
    try:
        driver = setup
        driver.get("https://www.redbus.in/")
        frm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "src")))
        frm.send_keys("Bangalore")
        frm.click()
        time.sleep(10)
        to= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dest")))
        to.send_keys("Chennai")
        to.click()
        time.sleep(2)
        dat = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "onwardCal")) )
        dat.send_keys("18-Jul-2024")
        dat.click()
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")))
        search_button.click()
        bus = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "bus-item")))
        bus[0].click()
        seat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//canvas[@class='pointer']")))
        seat.click()
    except NoSuchElementException as e:
        driver = setup
        proceed_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proceedButton")))
        proceed_button.click()
        print(f"element not found exception : {e}")



