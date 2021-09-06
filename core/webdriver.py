from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def project_dir():
    project_name = 'scanpy'
    base_dir = Path(__file__).resolve()
    while True:
        if base_dir.parent.name == project_name:
            return base_dir.parent

        base_dir = base_dir.parent


class Driver:
    def __init__(self, path):
        self.webdriver = webdriver.Chrome(
            executable_path=Path.joinpath(project_dir(), path)
        )

    def __enter__(self) -> WebDriver:
        return self.webdriver

    def __exit__(self, type, value, traceback):
        self.webdriver.close()


class Waiter:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def wait(self, condition: EC, seconds: int = 10):
        WebDriverWait(self.webdriver, seconds).until(condition)
