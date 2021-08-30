import pytest

from core.pages.pages import Login
from core.webdriver import Driver, base_dir
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
    with Driver(base_dir=base_dir()) as driver:
        login_page = Login(webdriver=driver, url=BASE_URL)
        login_page.open()
        yield login_page


@pytest.fixture
def fix_home(fix_login_page, fix_user):
    fix_login_page.login(username=fix_user.username, password=fix_user.password)
    yield fix_login_page.webdriver
