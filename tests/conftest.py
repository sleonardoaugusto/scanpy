import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from app import BASE_URL
from core.components.login import LoginPage
from core.webdriver import Driver


@pytest.fixture
def fix_login_page():
    driver = Driver()
    page = driver.open(BASE_URL)
    login_page = LoginPage(page)
    yield login_page
    page.close()


@pytest.fixture
def fix_homepage(fix_login_page):
    username = 'bobbybackupy'
    password = 'Argyleawesome123!'
    fix_login_page.login(username=username, password=password)
    yield fix_login_page.webdriver
    fix_login_page.webdriver.close()
