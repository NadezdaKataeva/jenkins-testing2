from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class FolderConfig(BasePage):

    def click_save(self):
        self.click((By.ID, "yui-gen6-button"))