import logging

from selenium.common.exceptions import TimeoutException, NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(filename='login.log', level=logging.INFO)


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


class LoginPage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.username = (By.ID, 'login_username')
        self.username_incorrect = (By.ID, 'username-message')
        self.captcha = (By.ID, 'px-captcha')
        self.password = (By.ID, 'login_password')
        self.password_incorrect = (By.ID, 'password-message')
        self.continue_btn = (By.ID, 'login_password_continue')
        self.login_btn = (By.ID, 'login_control_continue')
        self.secret_answer = (By.ID, 'secret_answer')

    def login(self, username, password):
        logging.info('Logging in...')
        self._set_username(username)
        self._captcha()
        self._set_password(password)

    def _set_username(self, username):
        logging.info(f'Filling username "{username}"')
        self.webdriver.find_element(*self.username).send_keys(username)
        self.webdriver.find_element(*self.continue_btn).click()
        self._validate_username()

    def _set_password(self, password):
        logging.info('Filling password')
        self.webdriver.find_element(*self.password).send_keys(password)
        self.webdriver.find_element(*self.login_btn).click()
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
                raise CaptchaRequired(error_message)
        except NoSuchFrameException:
            self.webdriver.switch_to.parent_frame()
