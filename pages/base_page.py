

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_to_page(self, url: str):
        self.driver.get(url)
        return self
