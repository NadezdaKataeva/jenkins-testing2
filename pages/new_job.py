from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

OK_BUTTON = (By.ID, "ok-button")


class NewJob(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_input_field_title(self):
        return self.get_text((By.XPATH, "//label[@for='name']"))

    def enter_item_name(self, name: str):
        self.get_wait().until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(name)

    def click_folder(self):
        self.click((By.XPATH, "//span[text()='Folder']"))

    def is_ok_button_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(OK_BUTTON)).is_enabled()

    def click_ok_button(self):
        self.click(OK_BUTTON)

    def click_freestyle(self):
        self.click(By.XPATH, "//span[text()='Freestyle project']")
