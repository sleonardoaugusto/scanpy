from pathlib import Path

import pytest

from core.pages.pages import Login, Home, Settings
from core.webdriver import Driver
from scrapper.scrapper import BASE_URL


@pytest.fixture(scope='session')
def fix_user():
    class User:
        username = 'bobbybackupy'
        password = 'Argyleawesome123!'
        secret_key = 'J6PMJ5GNXMGVU47A'

    return User()


@pytest.fixture(scope='session')
def fix_login_page():
    with Driver(path='webdrivers/chromedriver') as driver:
        login_page = Login(webdriver=driver, url=BASE_URL)
        login_page.open()
        yield login_page


@pytest.fixture(scope='session')
def fix_home_page(fix_login_page, fix_user):
    webdriver = fix_login_page.webdriver
    fix_login_page.login(username=fix_user.username, password=fix_user.password)
    home = Home(webdriver)
    yield home


@pytest.fixture(scope='session')
def fix_settings_page(fix_home_page, fix_user):
    webdriver = fix_home_page.webdriver
    fix_home_page.navbar.open_settings(fix_user.secret_key)
    settings = Settings(webdriver)
    yield settings


@pytest.fixture(autouse=True, scope='session')
def delete_logs():
    Path.unlink(Path('log.log'))
