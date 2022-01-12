import pytest
import requests

from requests.exceptions import ConnectionError
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.test_data import TestData as TD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


REMOTE_URL = 'http://127.0.0.1:4444/wd/hub'


def init_remote_driver_chrome():
    try:
        if requests.get(REMOTE_URL).status_code == 200:
            print('Grid is UP')

            return webdriver.Remote(command_executor=REMOTE_URL,
                                    desired_capabilities=DesiredCapabilities.CHROME.copy())
    except ConnectionError:
        pass

    print('Grid is DOWN')
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--window-size=1600,1080")
    chromeOptions.headless = True

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options=chromeOptions)


@pytest.fixture(params=['chrome'], scope='class', autouse=True)
def init_driver(request):
    driver = None
    driver = init_remote_driver_chrome()

    driver.get(TD.BASE_URL)
    if driver.title == "Sign in [Jenkins]":
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'j_username'))).send_keys(TD.LOGIN)
        driver.find_element(By.NAME, 'j_password').send_keys(TD.PASSWORD)
        driver.find_element(By.NAME, 'Submit').click()
    request.cls.driver = driver

    yield

    driver.quit()
