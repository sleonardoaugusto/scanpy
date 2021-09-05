from abc import ABC
from time import sleep
from typing import Union

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement(ABC):
    def __init__(self, webdriver: WebDriver = None):
        self.webdriver = webdriver

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        sleep(3)
        return self.webdriver.find_element(*locator)


class Page(PageElement, ABC):
    def __init__(self, webdriver: WebDriver, url: Union[str, None] = None):
        super().__init__(webdriver)
        self.url = url

    def open(self):
        self.webdriver.get(self.url)
