#https://trello.com/c/fD8Aq3gb/11-jn-3-verify-create-freestyle-page
from pages.dashboard_page import DashboardPage
from pages.folder_config import FolderConfig
from pages.freestyle_config import FreestyleConfig
from pages.job_freestyle import JobFreestyle
from pages.new_job import NewJob
from tests.base_test import BaseTest
from utils import jenkins_libs as jl

class TestFreestyle(BaseTest):

    jen_libs = jl.JenkinsLibs.jenkins_server

    def  test_create_freestyle_valid_name(self):
        freestyle_name = 'freestyle111'

        DashboardPage(self.driver).click_new_item()

        new_job = NewJob(self.driver)
        new_job.enter_item_name(freestyle_name)
        new_job.click_freestyle()
        assert new_job.is_ok_button_clickable()
        new_job.click_ok_button()

        freestyle_config = FreestyleConfig(self.driver)
        assert freestyle_config.get_current_url().endswith(f'/job/{freestyle_name}/configure')
        freestyle_config.click_save()

        job_freestyle = JobFreestyle(self.driver)
        assert job_freestyle.get_current_url().endswith(f'/job/{freestyle_name}/')
        assert freestyle_name in job_freestyle.get_page_title()

        self.jen_libs.delete_job(freestyle_name)
