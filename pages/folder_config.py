from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

SAVE_BTN = By.NAME, "Submit"

class FolderConfig(BasePage):

    def click_save(self):
        self.click(SAVE_BTN)