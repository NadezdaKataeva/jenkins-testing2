import jenkins
from config import test_data as td

class JenkinsLibs:

    jenkins_server = jenkins.Jenkins(td.TestData.BASE_URL, username=td.TestData.LOGIN, password=td.TestData.PASSWORD)
