from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.usernameLoc = (By.ID, 'email')
        self.passwordLoc = (By.ID, 'pass')
        self.login_buttonLoc = (By.NAME, 'login')

    def enter_username(self, userText):
        userName = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.usernameLoc))
        userName.send_keys(userText)

    def enter_password(self, passwordText):
        passWord = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.passwordLoc))
        passWord.send_keys(passwordText)

    def login(self):
        btn_Login = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(self.login_buttonLoc))
        btn_Login.click()
