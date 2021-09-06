from pathlib import Path

import pytest

from core.pages.pages import Login
from core.webdriver import Driver
from scrapper import BASE_URL


@pytest.fixture
def fix_user():
    class User:
        username = 'bobbybackupy'
        password = 'Argyleawesome123!'
        secret_key = 'J6PMJ5GNXMGVU47A'

    return User()


@pytest.fixture
def fix_login_page() -> Login:
    with Driver() as driver:
        login_page = Login(webdriver=driver, url=BASE_URL)
        login_page.open()
        yield login_page


@pytest.fixture
def fix_home(fix_login_page, fix_user):
    fix_login_page.login(username=fix_user.username, password=fix_user.password)
    yield fix_login_page.webdriver


@pytest.fixture(autouse=True, scope='session')
def delete_logs():
    Path.unlink(Path('log.log'))
