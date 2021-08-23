from abc import ABC


class PageElement(ABC):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)


class Page(PageElement, ABC):
    def __init__(self, webdriver, url=None):
        super().__init__(webdriver)
        self.url = url

    def open(self):
        self.webdriver.get(self.url)
