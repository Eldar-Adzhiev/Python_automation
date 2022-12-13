import time

import pytest
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By


class BaseTest:
    authorize = True

    @pytest.fixture(autouse=True)
    def prepare(self, browser, base_url, request, api_client):
        self.browser: ChromiumDriver = browser
        self.base_url: str = base_url

        self.api_client = api_client

        self.browser.get(self.base_url)
        time.sleep(3)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                cookie_dict = {
                    'domain': cookie.domain,
                    'name': cookie.name,
                    'value': cookie.value,
                    'secure': cookie.secure
                }
                self.browser.add_cookie(cookie_dict)

            self.browser.refresh()


class TestDevDivisionLogin(BaseTest):
    authorize = False

    LOGIN_BTN = (By.CSS_SELECTOR, 'button.e-button.e-button--secondary')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button.e-button.form__submit')

    def test_login(self, user):
        self.browser.find_element(*self.LOGIN_BTN).click()
        time.sleep(3)

        self.browser.find_element(*self.EMAIL_INPUT).send_keys(user.EMAIL)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(user.PASSWORD)
        self.browser.find_element(*self.SUBMIT_BTN).click()
        time.sleep(3)

        assert self.browser.find_element(By.CSS_SELECTOR, 'div.user-info p.text-lg').text == user.USERNAME


class TestDevDivisionMainPage(BaseTest):

    def test_auto_login(self, user):
        time.sleep(3)
        assert self.browser.find_element(By.CSS_SELECTOR, 'div.user-info p.text-lg').text == user.USERNAME
