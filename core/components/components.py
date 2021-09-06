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


class Location(PageElement):
    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.edit_location = (By.XPATH, '//button[@aria-label="Edit location"]')
        self.time_zone = (By.XPATH, '//*[@data-test="timezoneEdit"]')
        self.country = (By.XPATH, '//div[@data-test="countryEdit"]')
        self.street = (By.XPATH, '//input[@data-test="streetEdit"]')
        self.apt_suite = (By.XPATH, '//input[@data-test="street2Edit"]')
        self.city = (By.XPATH, '//div[@data-test="cityAutocompleteEdit"]//input')
        self.state_province = (By.XPATH, '//div[@data-test="stateDropdownEdit"]')
        self.zipcode = (By.XPATH, '//input[@data-test="zipEdit"]')
        self.country_code = (By.XPATH, '//div[@class="up-country-code"]')
        self.phone = (By.XPATH, '//input[@type="tel"]')
        self._load()

    def _load(self):
        Waiter(self.webdriver).wait(EC.presence_of_element_located(self.edit_location))
        self.edit()
        self.time_zone = self.find_element(self.time_zone).text
        self.country = self.find_element(self.country).text
        self.street = self.find_element(self.street).get_attribute('value')
        self.apt_suite = self.find_element(self.apt_suite).get_attribute('value')
        self.city = self.find_element(self.city).get_attribute('value')
        self.state_province = self.find_element(self.state_province).text
        self.zipcode = self.find_element(self.zipcode).get_attribute('value')
        self.country_code = self.find_element(self.country_code).text
        self.phone = self.find_element(self.phone).get_attribute('value')

    def edit(self):
        self.find_element(self.edit_location).click()
