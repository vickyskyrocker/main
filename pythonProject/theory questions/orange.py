#3) Go to https://www.orange.com/en --> handle cookies --> click on magazines -->
#click on ornage bussiness --> validate the title of the new window -->
#go back to prev window and close the browser.
#Use xpath and automate the below:
   # a.1> Go to amazon --> click on search box --> type iphone
# --> find the element in the result.
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.order(1)
def test_orange(setup):
    driver = setup
    driver.get("https://www.orange.com/en")
    time.sleep(10)
    accp_botton=driver.find_element(By.XPATH,"(//button)[1]")
    accp_botton.click()
    time.sleep(10)
    ori=driver.current_window_handle
    tit = ori.title()
    print("ori",tit)
    orange=driver.find_element(By.PARTIAL_LINK_TEXT,"Orange Business")
    orange.click()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    new=driver.current_window_handle
    newtitle=new.title()
    print("new",newtitle)
    driver.switch_to.window(ori)
    driver.close()




