import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.mark.order(2)
def test_login(setup):
    driver = setup
    driver.get("https://www.facebook.com")
    title = driver.title
    print(f"title is : {title}")
    assert title.__contains__("Facebook")
    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    username.send_keys("<EMAIL>")
    password.send_keys("<PASSWORD>")
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(5)

@pytest.mark.order(1)
def test_search(setup):
    driver = setup
    driver.get("https://www.google.com")
    textBox = driver.find_element(By.XPATH, "//textarea[contains(@title, 'Search')]")
    textBox.send_keys("Google search")
    time.sleep(5)
    
