from typing import Union

from selenium.webdriver.common.by import By

from core import pages
from core.pages.base import PageElement
from logger import logger


class NavBar(PageElement):
    avatar = (By.XPATH, '//li[@data-cy="user-menu"]/button')
    settings = (By.XPATH, '//span[@icon-name="settings"]')

    def open_settings(self, secret_key: Union[str, None] = None):
        logger.info(f'Opening settings page...')
        self.find_element(self.avatar).click()
        self.find_element(self.settings).click()
        self._authorize(secret_key)

    def _authorize(self, secret_key):
        if 'device-authorization' in self.webdriver.current_url:
            pages.DeviceAuthorization(self.webdriver, secret_key).authorize()
