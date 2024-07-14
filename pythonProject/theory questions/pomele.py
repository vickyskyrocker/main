import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class RedBus:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.redbus.in/"
        self.source_input = (By.ID, "src")
        self.destination_input = (By.ID, "dest")
        self.date_picker = (By.XPATH, "//input[@id='onward_cal']")
        self.search_button = (By.ID, "search_btn")

    def load(self):
        self.driver.get(self.url)
