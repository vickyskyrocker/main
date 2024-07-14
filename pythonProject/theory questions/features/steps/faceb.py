from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time



@given("User opens facebook login page")
def openUrl(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.maximize_window()
    self.driver.get("https://facebook.com")
    self.driver.maximize_window()


@when('Enter username "(?P<Username>.+)" and password "(?P<Password>.+)" in login page')
def user_pass(self,Username,Password):
    self.driver.find_element(By.NAME, 'email').send_keys(Username)
    self.driver.find_element(By.NAME, 'pass').send_keys(Password)

@then("Click on login button")
def login(self):
    self.driver.find_element(By.NAME, "login").click()
    time.sleep(5)



