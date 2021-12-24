from pages.dashboard_page import *
from pages.new_job import NewJob
from tests.base_test import BaseTest


class TestDashboardPage(BaseTest):

    def test_title(self):
        assert DashboardPage(self.driver).get_title() == DashboardPage.PAGE_TITLE

    def test_redirection_to_new_job_page(self):
        dash_board_page = DashboardPage(self.driver)
        dash_board_page.click_new_item()
        new_job_page = NewJob(self.driver)
        assert new_job_page.get_input_field_title() == 'Enter an item name'
