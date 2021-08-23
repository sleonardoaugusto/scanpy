from selenium.webdriver.common.by import By

from core.pages.base import PageElement


class NavBar(PageElement):
    user_avatar = (By.XPATH, '//*[@id="nav-right"]/ul/li[8]/button')
    settings = (By.XPATH, '//*[@id="nav-right"]/ul/li[8]/ul/li[3]/ul/li[1]/a')

    def open_settings(self):
        self.webdriver.find_element(*self.user_avatar).click()
        self.webdriver.find_element(*self.settings).click()
        return self.webdriver
