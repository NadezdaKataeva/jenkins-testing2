from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NewJob(BasePage):

    _title = By.XPATH, "//label[@for='name']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_input_field_title(self):
        return self.driver.find_element(self._title[0], self._title[1]).text
