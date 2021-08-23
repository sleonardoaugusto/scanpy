from core.pages.pages import Home, Settings


def test_get_settings(fix_home: Home):
    page = Home(fix_home).navbar.open_settings()
    settings = Settings(page, 'J6PMJ5GNXMGVU47A')
