# coding=utf-8
from selenium.webdriver.common.by import By

from .base_game_page import BaseGamePage


class PersonalDetailsFormPage(BaseGamePage):
    PERSONAL_DETAILS_FORM_PAGE = (By.XPATH,
                                  "//div[@class='personal-details__form']",
                                  'Locator for check of game card 3 page')

    def __init__(self):
        super().__init__(*self.PERSONAL_DETAILS_FORM_PAGE)

    def is_personal_details_form_page_presented(self):
        return self.is_opened()
