# coding=utf-8
from selenium.webdriver.common.by import By

from ...framework.pages.base_page import BasePage
from ...framework.elements.button import Button


class HomePage(BasePage):

    HOME_PAGE = (By.XPATH, '//p[@class="start__paragraph"]', 'Locator for check of home page')

    LINK_TO_NEXT_PAGE = Button(By.XPATH, '//a[@class="start__link"]', 'Button to go to the next page')

    def __init__(self):
        super().__init__(*self.HOME_PAGE)

    def is_home_page_presented(self):
        return self.is_opened()

    def go_to_next_page(self):
        self.LINK_TO_NEXT_PAGE.click()
