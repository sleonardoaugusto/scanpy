import logging

from pyotp import TOTP
from selenium.common.exceptions import TimeoutException, NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.components.navbar import NavBar
from core.pages.base import Page

logging.basicConfig(filename='login.log', level=logging.INFO)


class Home(Page):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.navbar = NavBar(webdriver)

    def settings(self):
        self.navbar.open_settings()
        secret_key = 'J6PMJ5GNXMGVU47A'
        settings = DeviceAuthorization(self.webdriver, secret_key)
        return settings


class IBaseException(Exception):
    def __init__(self, message):
        super().__init__(message)


class LoginError(IBaseException):
    pass


class InvalidUsername(IBaseException):
    pass


class InvalidPassword(IBaseException):
    pass


class CaptchaRequired(IBaseException):
    pass


class Login(Page):
    username = (By.ID, 'login_username')
    username_incorrect = (By.ID, 'username-message')
    captcha = (By.ID, 'px-captcha')
    password = (By.ID, 'login_password')
    password_incorrect = (By.ID, 'password-message')
    continue_btn = (By.ID, 'login_password_continue')
    login_btn = (By.ID, 'login_control_continue')
    secret_answer = (By.ID, 'secret_answer')

    def login(self, username, password):
        logging.info('Logging in...')
        self._set_username(username)
        self._captcha()
        self._set_password(password)

    def _set_username(self, username):
        logging.info(f'Filling username "{username}"')
        self.find_element(self.username).send_keys(username)
        self.find_element(self.continue_btn).click()
        self._validate_username()

    def _set_password(self, password):
        logging.info('Filling password')
        self.find_element(self.password).send_keys(password)
        self.find_element(self.login_btn).click()
        self._validate_password()

    def _validate_username(self):
        try:
            WebDriverWait(self.webdriver, 10).until(
                EC.presence_of_element_located(self.username_incorrect)
            )
            error_message = 'Invalid username'
            logging.error(error_message)
            raise InvalidUsername(error_message)
        except TimeoutException:
            logging.info('Username is valid.')

    def _validate_password(self):
        try:
            WebDriverWait(self.webdriver, 10).until(
                EC.presence_of_element_located(self.password_incorrect)
            )
            error_message = 'Invalid password'
            logging.error(error_message)
            raise InvalidPassword(error_message)
        except TimeoutException:
            logging.info('Password is valid.')

    def _captcha(self):
        try:
            self.webdriver.switch_to.frame('externalChallenge')
            human_verification = 'Please verify you are a human'
            page_text = self.webdriver.find_element_by_tag_name('body').text
            if human_verification in page_text:
                error_message = 'Captcha required'
                logging.error(error_message)
                breakpoint()
                raise CaptchaRequired(error_message)
        except NoSuchFrameException:
            self.webdriver.switch_to.parent_frame()


class DeviceAuthorization(Page):
    def __init__(self, webdriver, secret_key):
        super().__init__(webdriver)
        self.secret_key = secret_key
        self.otp_input = (By.ID, 'deviceAuthOtp_otp')
        self.otp_confirm_btn = (By.ID, 'next_continue')

    def authorize(self):
        totp = TOTP(self.secret_key)
        verification_code = totp.now()
        self._set_otp(verification_code)

    def _set_otp(self, verification_code):
        self.webdriver.find_element(*self.otp_input).send_keys(verification_code)
        self.webdriver.find_element(*self.otp_confirm_btn).click()


class Settings(Page):
    def __init__(self, webdriver, secret_key=None):
        super().__init__(webdriver)
        self._authorize(secret_key)

    def _authorize(self, secret_key):
        if secret_key:
            DeviceAuthorization(self.webdriver, secret_key).authorize()
