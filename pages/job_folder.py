from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class JobFolder(BasePage):

    def get_page_title(self):
        return self.get_text((By.TAG_NAME, "h1"))
