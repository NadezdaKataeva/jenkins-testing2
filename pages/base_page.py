from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = None

    def get_wait(self):
        if self.wait:
            return self.wait
        self.wait = WebDriverWait(self.driver, 5)
        return self.wait

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_to_page(self, url: str):
        self.driver.get(url)
        return self

    def is_visible(self, locator):
        try:
            self.get_wait().until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.get_wait().until(EC.visibility_of_element_located(locator)).text
