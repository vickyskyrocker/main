from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions


def run_test(browser, hub_url):
    if browser == "chrome":
        options = ChromeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Initialize the WebDriver with the Grid hub URL and browser options
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )

    try:
        # Open Facebook login page
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

        # Check if login was successful (you may need to adjust this based on the actual success criteria)
        try:
            driver.find_element(By.XPATH, "//div[text()='Home']")
            print(f"Login successful on {browser}")
        except:
            print(f"Login failed on {browser}")

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    hub_url = "http://192.168.0.101:4444/wd/hub"
    browsers = ["chrome"]  # Add other browsers as needed

    for browser in browsers:
        run_test(browser, hub_url)
