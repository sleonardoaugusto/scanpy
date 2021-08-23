import pytest

from app import BASE_URL
from core.pages.pages import Login
from core.webdriver import Driver


@pytest.fixture
def fix_login_page() -> Login:
    driver = Driver()
    login_page = Login(webdriver=driver.webdriver, url=BASE_URL)
    login_page.open()
    yield login_page
    login_page.webdriver.close()


@pytest.fixture
def fix_home(fix_login_page):
    username = 'bobbybackupy'
    password = 'Argyleawesome123!'
    fix_login_page.login(username=username, password=password)
    yield fix_login_page.webdriver
