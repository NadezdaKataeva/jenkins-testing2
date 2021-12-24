from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NewJob(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_input_field_title(self):
        return self.get_text((By.XPATH, "//label[@for='name']"))
