from selenium.webdriver.chrome.webdriver import WebDriver

from core.pages import Login, Home, Settings
from core.webdriver import Driver, base_dir
from db import Database
from schemas.schemas import AccountSchema

BASE_URL = 'https://www.upwork.com/ab/account-security/login'


class Scrapper:
    def __init__(
        self, webdriver: WebDriver, username: str, password: str, secret_key: str
    ):
        self.webdriver = webdriver
        self.secret_key = secret_key
        self._login(username, password)

    def _login(self, username: str, password: str):
        page = Login(webdriver=self.webdriver, url=BASE_URL)
        page.open()
        page.login(username=username, password=password)

    def open_settings(self):
        home = Home(self.webdriver)
        home.navbar.open_settings(self.secret_key)


class SettingsScrappy(Scrapper):
    def account_info(self) -> dict:
        self.open_settings()
        account = Settings(self.webdriver).navbar.contact_info.account
        return AccountSchema(
            user_id=account.user_id,
            name=account.first_name,
            surname=account.last_name,
            email=account.email,
        ).dict()


def run(username: str, password: str, secret_key: str):
    with Driver(base_dir=base_dir()) as driver:
        settings_scrappy = SettingsScrappy(driver, username, password, secret_key)
        db = Database()
        db.save(settings_scrappy.account_info())
