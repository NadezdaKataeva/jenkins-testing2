from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.test_data import TestData as TD

DELETE_FOLDER = By.XPATH, "//*[@title='Delete Folder']"
CONFIRM_DELETE = By.NAME, "Submit"

class JobFolder(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.url = TD.DASHBOARD_URL + name

    def get_page_title(self):
        return self.get_text((By.TAG_NAME, "h1"))

    def click_delete_folder(self):
        self.click(DELETE_FOLDER)
        if self.is_visible(CONFIRM_DELETE):
            self.click(CONFIRM_DELETE)

