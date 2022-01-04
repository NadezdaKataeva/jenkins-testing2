from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class BuildHistory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_panel(self):
        return self.get_text((By.XPATH, '//*[@id="main-panel"]'))


