from core.pages.pages import Home, Settings


def test_account_info(fix_user, fix_home):
    home = Home(fix_home)
    home.navbar.open_settings(fix_user.secret_key)
    account = Settings(fix_home).navbar.contact_info.account
    assert account.first_name == 'Bobby'
    assert account.last_name == 'Backupy'
    assert account.email == 'bob.worker+backupaccount@argyle.io'


def test_location_info(fix_user, fix_home):
    home = Home(fix_home)
    home.navbar.open_settings(fix_user.secret_key)
    location = Settings(fix_home).navbar.contact_info.location
    assert location.time_zone == 'UTC+02:00 Israel'
    assert location.country == 'United States'
    assert location.street == 'Party street 100'
    assert location.apt_suite == '1'
    assert location.city == 'Miami'
    assert location.state_province == 'FL'
    assert location.zipcode == '123456'
    assert location.phone == '9176987366'
