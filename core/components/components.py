from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core import pages
from core.pages.base import PageElement
from core.webdriver import Waiter


class SettingsNavBar(PageElement):
    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.contact_info = pages.ContactInfo(webdriver)


class Account(PageElement):
    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.user_id = (By.XPATH, '//div[@data-test="userId"]')
        self.first_name = (By.XPATH, '//input[@data-test="firstNameEdit"]')
        self.last_name = (By.XPATH, '//input[@data-test="lastNameEdit"]')
        self.email = (By.XPATH, '//input[@data-test="emailEdit"]')
        self.edit_account = (By.XPATH, '//button[@aria-label="Edit account"]')
        self._load()

    def _load(self):
        Waiter(self.webdriver).wait(EC.presence_of_element_located(self.user_id))
        self.user_id = self.find_element(self.user_id).text
        self.edit()
        self.first_name = self.find_element(self.first_name).get_attribute('value')
        self.last_name = self.find_element(self.last_name).get_attribute('value')
        self.email = self.find_element(self.email).get_attribute('value')

    def edit(self):
        self.find_element(self.edit_account).click()
