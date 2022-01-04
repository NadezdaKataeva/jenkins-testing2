from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.build_history import BuildHistory
from pages.dashboard_page import DashboardPage
from tests.base_test import BaseTest

URL = "http://localhost:8080/legend"
ICON_LEGEND_LIST = (By.XPATH, "//*[@id='main-panel']")
ICON_LEGEND_LINK = (By.XPATH, "//*[@id='rss-bar']/a[1]")

class TestBuildHistory(BaseTest):

    def test_check_icon_legend_availability(self):
        # Click by link “Build History”
        DashboardPage(self.driver).click_build_history()

        # ER:
        # The link is clickable
        # Find the "Icon legend" link. Click.
        assert BasePage(self.driver).is_visible(ICON_LEGEND_LINK)
        assert BasePage(self.driver).is_clickable(ICON_LEGEND_LINK)
        BasePage(self.driver).click(ICON_LEGEND_LINK)

        # User redirected to the next page.
        # ER: Page URL is {base url}/legend
        assert BasePage.get_current_url(self).endswith("/legend")
        assert BasePage.get_current_url(self) == URL

        # ER:
        # The created page has the dictionary of all meanings of the signs (id = "main-panel")
        assert BasePage(self.driver).get_text(ICON_LEGEND_LIST)

