from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.TestData import TestData as TD

PREVIEW = (By.XPATH, "//a[text() = 'Preview']")
HIDEPREVIEW = (By.XPATH, "//a[text() = 'Hide preview']")

class FreestyleConfig(BasePage):

    GENERAL = (By.XPATH, "//div[@class='tab config-section-activator config_general active']")
    SOURCECM = (By.XPATH, "//div[@class='tab config-section-activator config_source_code_management']")
    BUILDTRIGGERS = (By.XPATH, "//div[@class= 'tab config-section-activator config_build_triggers']")
    BUILDENVIRONMENT = (By.XPATH, "//div[@class='tab config-section-activator config_build_environment']")
    TEXT_AREA_DESCRIPTION =(By.XPATH, "//textarea[@name='description']")
    HIDEPREVIEW = (By.XPATH, "//a[text() = 'Hide preview']")

    def __init__(self, driver, name):
        super().__init__(driver)
        self.url = TD.DASHBOARD_URL + f'job/{name}/configure'

    def is_tab_general_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(self.GENERAL)).is_enabled()

    def is_tab_sourcecm_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(self.SOURCECM)).is_enabled()

    def is_tab_buildtriggers_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(self.BUILDTRIGGERS)).is_enabled()

    def is_tab_buildenvironment_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(self.BUILDENVIRONMENT)).is_enabled()

    def is_text_area_description_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(self.TEXT_AREA_DESCRIPTION)).is_enabled()

    def is_preview_link_clickable(self):
        return self.get_wait().until(EC.visibility_of_element_located(PREVIEW)).is_enabled()

    def click_preview_link(self):
            self.click(PREVIEW)

    def is_hide_link_clickable(self):
       return self.get_wait().until(EC.visibility_of_element_located(HIDEPREVIEW)).is_enabled()

    def click_hidepreview_link(self):
            self.click((By.XPATH, "//a[text() = 'Hide preview']"))

    def click_save(self):
        self.click((By.XPATH, "//*[@type='submit']"))