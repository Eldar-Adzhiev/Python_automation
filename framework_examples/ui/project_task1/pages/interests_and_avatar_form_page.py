# coding=utf-8
from selenium.webdriver.common.by import By

from .base_game_page import BaseGamePage
from ...framework.elements.checkbox import CheckBox
from ...framework.elements.button import Button
from ...framework.elements.text import Text

from ...framework.utils.random_util import random_list_element
from ...framework.utils.autoit_utils import AutoItUtils


class InterestsAndAvatarFormPage(BaseGamePage):
    INTERESTS_AND_AVATAR_PAGE = (By.XPATH, "//div[@class='avatar-and-interests__form']", 'Locator for check of game card 2 page')

    UPLOAD_IMAGE_BUTTON = Button(By.XPATH, "//a[contains(@class,'upload-button')]", "Locator for upload image button")

    INTERESTS_CHECKBOX = CheckBox(By.XPATH,
                                  "//div[contains(@class,'interests-list__item')]//label",
                                  "Locator for all interests checkbox")
    UNSELECT_ALL_INTERESTS = CheckBox(By.XPATH,
                                      "//label[@for='interest_unselectall']",
                                      "Locator for unselect all interests")
    PERSONAL_DETAILS_FORM = Text(By.XPATH, "//div[@class='personal-details__form']", "Locator")
    BUTTON_NEXT = Button(By.XPATH, "//button[text()='Next']", "Locator for button in 2 card")

    def __init__(self):
        super().__init__(*self.INTERESTS_AND_AVATAR_PAGE)

    def is_interests_and_avatar_form_page_presented(self):
        return self.is_opened()

    def unselect_all_checkbox(self):
        self.UNSELECT_ALL_INTERESTS.click()

    def select_interests(self, what):
        self.unselect_all_checkbox()
        count = 0
        pool = []
        while count < what:
            element = random_list_element(self.INTERESTS_CHECKBOX.get_elements(), 1)
            if (element[0].get_attribute('for') in ["interest_unselectall", "interest_selectall"]) or (element[0] in pool):
                continue
            element[0].click()
            count += 1
            pool.append(element[0])

    def click_upload_image(self):
        self.UPLOAD_IMAGE_BUTTON.click()

    def upload_image(self, window_handle, path_to_file):
        upload_file = AutoItUtils()
        upload_file.upload_image(window_handle, path_to_file)

    def go_to_personal_details_card(self):
        self.BUTTON_NEXT.click()
