from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = None
        self.sort_wait = None

    def get_short_wait(self):
        if self.sort_wait:
            return self.sort_wait
        self.wait = WebDriverWait(self.driver, 1)
        return self.wait

    def get_wait(self):
        if self.wait:
            return self.wait
        self.wait = WebDriverWait(self.driver, 4)
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
        element = self.get_wait().until(EC.visibility_of_element_located(locator))
        if element.text:
            return element.text
        else:
            return element.get_attribute('value')
