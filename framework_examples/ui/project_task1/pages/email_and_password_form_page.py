# coding=utf-8
from selenium.webdriver.common.by import By

from .base_game_page import BaseGamePage
from ...framework.elements.form import Form
from ...framework.elements.dropdown import Dropdown
from ...framework.elements.checkbox import CheckBox
from ...framework.elements.button import Button

from ...framework.utils.random_util import get_random_password_and_email
from ...framework.utils.random_util import random_list_element


class EmailAndPasswordFormPage(BaseGamePage):

    EMAIL_AND_PASSWORD_FORM_PAGE = (By.XPATH, '//div[@class="login-form__container"]', 'Locator for check of game card 1 page')

    PASSWORD_FORM = Form(By.XPATH, "//input[contains(@placeholder,'Password')]", "Locator for password entry form")
    EMAIL_FORM = Form(By.XPATH, "//input[contains(@placeholder,'email')]", "Locator for email entry form")
    DOMAIN_FORM = Form(By.XPATH, "//input[contains(@placeholder,'Domain')]", "Locator for domain entry form")
    DROPDOWN = Dropdown(By.XPATH, "//div[@class='dropdown__field']", "Locator for dropdown field")
    DROPDOWN_LIST = Dropdown(By.XPATH, "//div[@class='dropdown__list-item']", "Locator of list values in dropdown")
    CHECKBOX = CheckBox(By.XPATH, "//span[@class='checkbox__box']", "//span[@class='checkbox__box']")

    BUTTON_NEXT = Button(By.XPATH, "//a[@class='button--secondary']", "Locator for button next")

    def __init__(self):
        super().__init__(*self.EMAIL_AND_PASSWORD_FORM_PAGE)

    def is_email_and_password_form_page(self):
        return self.is_opened()

    def fill_in_the_form(self):
        password, email, domain = get_random_password_and_email()

        self.input_password(password)
        self.input_email(email)
        self.input_domain(domain)
        self.select_value_in_dropdown()
        self.select_checkbox()

    def input_password(self, password):
        self.PASSWORD_FORM.clear_form()
        self.PASSWORD_FORM.send_keys(password)

    def input_email(self, email):
        self.EMAIL_FORM.clear_form()
        self.EMAIL_FORM.send_keys(email)

    def input_domain(self, domain):
        self.DOMAIN_FORM.clear_form()
        self.DOMAIN_FORM.send_keys(domain)

    def select_value_in_dropdown(self):
        self.DROPDOWN.click()
        element = random_list_element(self.DROPDOWN_LIST.get_elements(), 1)
        element[0].click()

    def select_checkbox(self):
        self.CHECKBOX.click()

    def go_to_interests_and_avatar_card(self):
        self.BUTTON_NEXT.click()
