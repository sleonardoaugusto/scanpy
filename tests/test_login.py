import pytest

from core.components.login import InvalidPassword, InvalidUsername


def test_username_should_be_invalid(fix_login_page):
    with pytest.raises(InvalidUsername):
        username = 'C9KePUHRAs9ZQfbz'
        fix_login_page.login(username=username, password='')


def test_password_should_be_invalid(fix_login_page):
    with pytest.raises(InvalidPassword):
        username = 'bobbybackupy'
        fix_login_page.login(username=username, password='fail!')


def test_should_login(fix_login_page):
    username = 'bobbybackupy'
    password = 'Argyleawesome123!'
    fix_login_page.login(username=username, password=password)
