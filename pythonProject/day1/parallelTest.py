import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(params=["chrome", "edge"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    hub_url = "http://172.21.144.1:4444/wd/hub"
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    yield driver
    driver.quit()


def test_facebook_login(driver):
    driver.get("https://www.facebook.com/")

    # Find and fill the email and password fields
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")

    email_field.send_keys("your-email@example.com")
    password_field.send_keys("your-password")

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the result
    time.sleep(5)

