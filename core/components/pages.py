from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core.components.navbar import NavBar


class SettingsPage:
    def __init__(self, webdriver: WebDriver, verification_code):
        self.webdriver = webdriver
        self.otp_input = (By.ID, 'deviceAuthOtp_otp')
        self.otp_confirm_btn = (By.ID, 'next_continue')
        self._set_otp(verification_code)

    def _set_otp(self, verification_code):
        self.webdriver.find_element(*self.otp_input).send_keys(verification_code)
        self.webdriver.find_element(*self.otp_confirm_btn).click()
        # TODO: scrapy profile settings page


class HomePage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.navbar = NavBar(webdriver)

    def settings(self):
        self.navbar.open_settings()
        verification_code = int(input('Enter 6-digit code here'))
        settings = SettingsPage(self.webdriver, verification_code)
        return settings
