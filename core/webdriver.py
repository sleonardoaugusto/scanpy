from pathlib import Path

from selenium import webdriver


class Driver:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DRIVER_PATH = 'webdrivers/chromedriver'

    def __init__(self):
        self.webdriver = webdriver.Chrome(
            Path.joinpath(self.BASE_DIR, self.DRIVER_PATH)
        )

    def open(self, url):
        self.webdriver.get(url)
        return self.webdriver

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)
