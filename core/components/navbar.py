from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class NavBar:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver
        self.user_avatar = (By.XPATH, '//*[@id="nav-right"]/ul/li[8]/button')
        self.settings_menu_item = (
            By.XPATH,
            '//*[@id="nav-right"]/ul/li[8]/ul/li[3]/ul/li[1]/a',
        )

    def open_settings(self):
        self.webdriver.find_element(*self.user_avatar).click()
        self.webdriver.find_element(*self.settings_menu_item).click()
