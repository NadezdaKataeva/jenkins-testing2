from pages.base_page import BasePage
from config.test_data import TestData as TD
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    PAGE_TITLE = 'Dashboard [Jenkins]'

    DASHBOARD_MENU_ANCHOR = (By.CSS_SELECTOR, 'a.breadcrumbBarAnchor')
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW = (By.XPATH, '//ul[@id="breadcrumbs"]/li[@class="children"]')
    RIGHT_ARROW_MENU = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_MENU_ICON = (By.XPATH, '//div[@id="breadcrumb-menu-target"]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = TD.BASE_URL

    def click_new_item(self):
        self.click((By.XPATH, '//a[@title="New Item"]'))
