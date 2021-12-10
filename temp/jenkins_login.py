"""
Login into local Jenkins
TODO: set username and password to actual values
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# test data
BASE_URL = 'http://localhost:8080'
username = 'user'
password = '12345678'

# initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)

# login
driver.get(BASE_URL)
wait.until(EC.presence_of_element_located((By.ID, 'j_username'))).send_keys(username)
driver.find_element(By.NAME, 'j_password').send_keys(password)
driver.find_element(By.NAME, 'Submit').click()

assert wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == 'Welcome to Jenkins!'

sleep(10)
sleep(5)
