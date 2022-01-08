import pytest

from pages.dashboard_page import DashboardPage
from pages.folder_config import FolderConfig
from pages.job_folder import JobFolder
from pages.new_job import NewJob
from tests.base_test import BaseTest


class TestFolder(BaseTest):
    @pytest.mark.skip
    def test_create_folder_valid_name(self):
        folder_name = 'testfolder123'

        DashboardPage(self.driver).click_new_item()

        new_job = NewJob(self.driver)
        new_job.enter_item_name(folder_name)
        new_job.click_folder()
        assert new_job.is_ok_button_clickable()
        new_job.click_ok_button()

        folder_config = FolderConfig(self.driver)
        assert folder_config.get_current_url().endswith(f'/job/{folder_name}/configure')
        folder_config.click_save()

        job_folder = JobFolder(self.driver)
        assert job_folder.get_current_url().endswith(f'/job/{folder_name}/')
        assert job_folder.get_page_title() == folder_name
