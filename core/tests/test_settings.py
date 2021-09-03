from core.pages.pages import Home, Settings


def test_get_account_info(fix_user, fix_home):
    home = Home(fix_home)
    home.navbar.open_settings(fix_user.secret_key)
    account = Settings(fix_home).navbar.contact_info.account
    assert account.first_name == 'Bobby'
    assert account.last_name == 'Backupy'
    assert account.email == 'bob.worker+backupaccount@argyle.io'
