from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pomfun import test_book_ticket


chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://www.redbus.in/")
test_book_ticket(driver)



