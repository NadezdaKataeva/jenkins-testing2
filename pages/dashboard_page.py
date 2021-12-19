from pages.base_page import BasePage
from config.test_data import TestData as TD
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    PAGE_TITLE = 'Dashboard [Jenkins]'

    _new_item = By.XPATH, "//a[@title='New Item']"
    _dashboard_menu_anchor = (By.CSS_SELECTOR, 'a.breadcrumbBarAnchor')
    _menu_selector = (By.ID, 'menuSelector')
    _right_arrow = (By.XPATH, '//ul[@id="breadcrumbs"]/li[@class="children"]')
    _right_arrow_menu = (By.XPATH, '//a[@href="/view/all/"]')
    _right_arrow_menu_icon = (By.XPATH, '//div[@id="breadcrumb-menu-target"]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(TD.BASE_URL)

    def click_new_item(self):
        self.driver.find_element(self._new_item[0], self._new_item[1]).click()
