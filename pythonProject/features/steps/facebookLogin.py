from behave import *
from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

use_step_matcher("re")


@given("User opens facebook login page")
def openUrl(context):
    service = Service(executable_path=ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get('https://facebook.com')
    context.driver.maximize_window()
    time.sleep(2)
    assert 'Facebook' in context.driver.title


@when("Enter Username and Password in login page")
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('User')
    context.driver.find_element(By.NAME, 'pass').send_keys('PASSWORD')


@then("Click on login button")
def step_impl(context):
    context.driver.find_element(By.NAME, "login").click()
    time.sleep(5)


@when('I enter username "(?P<username>.+)" and password "(?P<password>.+)"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, 'email').send_keys(username)
    context.driver.find_element(By.ID, 'pass').send_keys(password)

