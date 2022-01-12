
from selenium.webdriver.common.by import By

import pytest


from pages.dashboard_page import DashboardPage
from pages.folder_config import FolderConfig
from pages.job_folder import JobFolder
from pages.new_job import NewJob
from tests.base_test import BaseTest


class TestFolder(BaseTest):
    folder_name = 'testfolder1180'

    def test_create_folder_valid_name(self):
        DashboardPage(self.driver).click_new_item()
        new_job = NewJob(self.driver)
        new_job.enter_item_name(self.folder_name)
        new_job.click_folder()
        assert new_job.is_ok_button_clickable()
        new_job.click_ok_button()

        folder_config = FolderConfig(self.driver)
        assert folder_config.get_current_url().endswith(f'/job/{self.folder_name}/configure')
        folder_config.click_save()

        job_folder = JobFolder(self.driver, self.folder_name)
        assert job_folder.get_current_url().endswith(f'/job/{self.folder_name}/')
        assert job_folder.get_page_title() == self.folder_name
    @pytest.mark.skip
    def test_delete_created_folder(self):
        job_folder = JobFolder(self.driver, self.folder_name)
        job_folder.click_delete_folder()
        assert job_folder.get_current_url() == DashboardPage.DASHBOARD_URL

        dashboard = DashboardPage(self.driver)
        table_jobs = dashboard.get_jobs_names_from_table()

        assert self.folder_name not in table_jobs
