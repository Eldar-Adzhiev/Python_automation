import logging

import allure
import pytest
from selenium.webdriver.chromium.webdriver import ChromiumDriver
import typing
from main.ui.page_object.simple.page import BasePage

T = typing.TypeVar('T', bound=BasePage)


class BaseUISuiteTest:

    base_url: str
    browser: ChromiumDriver
    logger: logging.Logger
    ui_config: dict

    @pytest.fixture(autouse=True)
    def prepare(self, browser, base_url, logger, ui_config, repo_root):
        self.repo_root = repo_root

        self.browser: ChromiumDriver = browser
        self.base_url: str = base_url
        self.logger: logging.Logger = logger
        self.ui_config: dict = ui_config

        self.logger.info('PREPARE DONE')

    @allure.step('Getting page {page_class}')
    def get_page(self, page_class: typing.Type[T]) -> T:
        # Установка кук
        # Проброс гет-параметров
        # etc
        self.browser.get(self.base_url + page_class.path)
        # document.readyState | 'complete', 'eager',
        page = page_class(self.browser)
        assert page.is_page_loaded(), f'{page.path} не загрузилась!'
        return page
