from pages.base_page import BasePage
from config.TestData import TestData as TD
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    PAGE_TITLE = 'Dashboard [Jenkins]'

    DASHBOARD_MENU_ANCHOR = (By.CSS_SELECTOR, 'a.breadcrumbBarAnchor')
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW = (By.XPATH, '//ul[@id="breadcrumbs"]/li[@class="children"]')
    RIGHT_ARROW_MENU = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_MENU_ICON = (By.XPATH, '//div[@id="breadcrumb-menu-target"]/div')
    DASHBOARD_TABLE = By.XPATH, '//*[@id="projectstatus"]'

    DASHBOARD_URL= TD.DASHBOARD_URL


    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(self.DASHBOARD_URL)

    def click_new_item(self):
        self.click((By.XPATH, '//a[@title="New Item"]'))

    def is_job_exist(self, job_name):
        return self.is_visible((By.XPATH, f"//a[text()='{job_name}']"))


