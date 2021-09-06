from selenium.webdriver.common.by import By

from core import pages
from core.pages.base import PageElement
from logger import logger


class NavBar(PageElement):
    avatar = (By.XPATH, '//li[@data-cy="user-menu"]/button')
    settings = (By.XPATH, '//span[@icon-name="settings"]')

    def open_settings(self, secret_key=None, secret_answer=None):
        logger.info(f'Opening settings page...')
        self.find_element(self.avatar).click()
        self.find_element(self.settings).click()
        self._authorize(secret_key, secret_answer)

    def _authorize(self, secret_key, secret_answer):
        if 'device-authorization' in self.webdriver.current_url:
            if secret_key:
                auth_page = pages.OTPAuth(self.webdriver, secret_key)
            else:
                auth_page = pages.AnswerAuth(self.webdriver, secret_answer)
            pages.DeviceAuthorization(auth_page).authorize()
