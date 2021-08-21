from core.components.pages import HomePage


def test_get_settings(fix_homepage):
    HomePage(fix_homepage).settings()
