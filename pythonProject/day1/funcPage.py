from pomHomeClass import Login_Page
import time

def login(driver):
    loginPage = Login_Page(driver)
    loginPage.enter_username("User")
    loginPage.enter_password("password")
    loginPage.login()
    time.sleep(5)
