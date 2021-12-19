import pytest
import requests
from requests.exceptions import ConnectionError
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from config.test_data import TestData as TD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


REMOTE_URL = 'http://127.0.0.1:4444/wd/hub'


def is_grid_up():
    try:
        response = requests.get(REMOTE_URL)
    except ConnectionError:
        print('Grid is DOWN!')
        return False

    print('Grid is UP!')
    return response.status_code == 200


def init_remote_driver_chrome():
    if is_grid_up():
        desired_capabilities = DesiredCapabilities.CHROME.copy()
        driver = webdriver.Remote(command_executor=REMOTE_URL,
                                  desired_capabilities=desired_capabilities)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1600,1080")
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return driver


@pytest.fixture(params=['chrome'], scope='class', autouse=True)
def init_driver(request):
    driver = init_remote_driver_chrome()

    driver.get(TD.BASE_URL)
    if driver.title == "Sign in [Jenkins]":
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'j_username'))).send_keys(TD.LOGIN)
        driver.find_element(By.NAME, 'j_password').send_keys(TD.PASSWORD)
        driver.find_element(By.NAME, 'Submit').click()
    request.cls.driver = driver

    yield

    driver.quit()
