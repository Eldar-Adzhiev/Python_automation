import logging

import allure

from main.ui.page_object.simple.downloadpage import DownloadsPage
from main.ui.page_object.simple.page import BasePage
from selenium.webdriver.common.by import By

from main.ui.page_object.advanced.elements import Page, Element


logger = logging.getLogger('test')


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '#id-search-field')
    DOWNLOAD_LINK = (By.CSS_SELECTOR, '#downloads > a')
    CLICK_THESE = (By.CSS_SELECTOR, '.click-these')


class MainPage(BasePage):
    """
        PageObject: https://python.org.
    """

    path = '/'
    locators = MainPageLocators()

    def get_click_these(self):
        return self._find_element(*self.locators.CLICK_THESE)

    def is_page_loaded(self) -> bool:
        self.wait.until(
            lambda _: self._find_element(*self.locators.SEARCH_INPUT)
        )
        return True

    def search_by_text(self, text):
        logger.info(f'I am searching by text {text}')
        self._send_keys(self.locators.SEARCH_INPUT[0], self.locators.SEARCH_INPUT[1], text)

    @allure.step('going to downloads')
    def go_to_downloads(self) -> DownloadsPage:
        self._click(*self.locators.DOWNLOAD_LINK)
        return DownloadsPage(self._driver)


class DescrMainPage(Page):
    """
        PageObject: https://python.org.
    """

    path = '/'

    search_input = Element(By.CSS_SELECTOR, '#id-search-field', 'Поисковые инпута')
