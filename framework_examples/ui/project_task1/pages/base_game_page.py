# coding=utf-8
from selenium.webdriver.common.by import By

from ...framework.pages.base_page import BasePage
from ...framework.elements.button import Button
from ...framework.elements.text import Text


class BaseGamePage(BasePage):

    BUTTON_FOR_HIDE_HELP_FORM = Button(By.XPATH,
                                       "//button[contains(@class,'help-form__send')]",
                                       "Locator for button for hide help form")
    HELP_FORM = Text(By.XPATH, "//div[contains(@class,'help-form')][1]", "Locator for help form")
    HELP_FORM_ATTR_IS_HIDDEN = 'is-hidden'

    BUTTON_ACCEPT_COOKIES = Button(By.XPATH,
                                   "//div[@class='cookies']//button[@name='button'][1]",
                                   "Locator for accept cookies")
    COOKIES_BANNER = Text(By.XPATH, "//div[@class='cookies']", "Locator for cookies banner")

    TIMER = Text(By.XPATH, "//div[contains(@class,'timer')]", "Locator for timer in page")

    def hide_the_help_form(self):
        self.BUTTON_FOR_HIDE_HELP_FORM.click()

    def get_attr_help_form_is_hidden(self):
        return self.HELP_FORM.get_attribute_class()

    def accept_cookies(self):
        self.BUTTON_ACCEPT_COOKIES.click()

    def is_cookies_banner_presented(self):
        return self.COOKIES_BANNER.is_displayed()

    def get_time_in_timer(self):
        return self.TIMER.get_text()
