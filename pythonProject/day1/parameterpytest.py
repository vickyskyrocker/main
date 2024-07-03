import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("search_term, expected_Text", [
    ("pytest", "pytest: helps you write better programs"),
    ("Selenium", "Selenium"),
    ("Python", "Welcome to Python.org"),
])

def test_gSearch(driver, search_term, expected_Text):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.XPATH, "//textarea[contains(@title, 'Search')]")
    search_box.send_keys(search_term)
    search_box.submit()
    time.sleep(5)
    print("pagesource is : " + driver.page_source)
    assert expected_Text in driver.page_source
