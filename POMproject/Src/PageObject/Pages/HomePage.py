from Src.PageObject.Locators import Locator


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element("id", Locator.logo)
        self.search_text = driver.find_element("name", Locator.search_text)
        self.submit = driver.find_element("name", Locator.submit)

    def get_search_text(self):
        return self.search_text

    def get_submit(self):
        return self.submit

    def get_web_page_logo(self):
        return self.logo
