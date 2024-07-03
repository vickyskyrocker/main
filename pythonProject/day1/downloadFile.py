import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def set_chrome_options(download_dir):
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options


def validate_download(download_dir, file_name):
    file_path = os.path.join(download_dir, file_name)
    return os.path.isfile(file_path) and os.path.getsize(file_path) > 0


def download_file(driver, downloadButtonLoc, download_dir):
    download_button = driver.find_element(By.ID, downloadButtonLoc)
    download_button.click()
    time.sleep(5)
    if validate_download(download_dir, "sampleFile.jpeg"):
        print("File downloaded and validated successfully.")
    else:
        print("File download failed or file not found.")


def main():
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)
    chrome_options = set_chrome_options(download_dir)
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://demoqa.com/upload-download")
    wait = WebDriverWait(driver, 1000)
    download_button_id = "downloadButton"
    wait.until(EC.presence_of_element_located((By.ID, download_button_id)))
    download_file(driver, download_button_id, download_dir)
    time.sleep(5)

if __name__ == "__main__":
    main()
