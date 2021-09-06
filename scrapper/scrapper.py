from selenium.webdriver.chrome.webdriver import WebDriver

from core.pages import Login, Home, Settings
from core.utils import retry
from core.webdriver import Driver
from db import Database

BASE_URL = 'https://www.upwork.com/ab/account-security/login'


class Scrapper:
    def __init__(
        self,
        webdriver: WebDriver,
        username: str,
        password: str,
        secret_key: str,
        secret_answer: str,
    ):
        self.webdriver = webdriver
        self.secret_key = secret_key
        self.secret_answer = secret_answer
        self._login(username, password)

    def _login(self, username: str, password: str):
        page = Login(webdriver=self.webdriver, url=BASE_URL)
        page.open()
        page.login(username=username, password=password)

    def open_settings(self):
        page = Home(self.webdriver)
        page.navbar.open_settings(self.secret_key, self.secret_answer)


class SettingsScrappy(Scrapper):
    def __init__(
        self,
        webdriver: WebDriver,
        username: str,
        password: str,
        secret_key: str,
        secret_answer: str,
    ):
        super().__init__(webdriver, username, password, secret_key, secret_answer)
        self.open_settings()

    def account_info(self) -> dict:
        return Settings(self.webdriver).navbar.contact_info.info()


@retry(retries=3)
def run(
    *, username: str, password: str, secret_key: str = None, secret_answer: str = None
):
    with Driver(path='webdrivers/chromedriver') as driver:
        settings_scrappy = SettingsScrappy(
            driver, username, password, secret_key, secret_answer
        )
        db = Database()
        db.save(settings_scrappy.account_info())
