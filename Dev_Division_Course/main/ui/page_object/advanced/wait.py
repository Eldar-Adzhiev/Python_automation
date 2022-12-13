from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Callable, List, Union


class Timeouts:
    """Таймауты для ui-тестов."""

    # Для поиска элемента в Element/Elements
    SEARCH = 5

    # Для ожиданий
    SHORT_WAIT = 2
    MEDIUM_WAIT = 5
    LONG_WAIT = 15


class Wait:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def until(
            self,
            method: Callable,
            *,
            timeout: Timeouts,
            ignored_exceptions: Union[Exception, List[Exception]] = None,
            message: str = ''
    ):
        return WebDriverWait(
            self.driver, timeout, ignored_exceptions=ignored_exceptions
        ).until(
            method,
            message,
        )
