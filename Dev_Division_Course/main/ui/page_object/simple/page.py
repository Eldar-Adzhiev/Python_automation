import logging
from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC


from abc import abstractmethod

logger = logging.getLogger('test')


class BasePage:

    @property
    @abstractmethod
    def path(self):
        raise NotImplementedError

    @abstractmethod
    def is_page_loaded(self) -> bool:
        raise NotImplementedError

    def __init__(self, driver):
        logger.info(f'Initializing page {self.__class__.__name__}...')
        self._driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self._driver, 10)
        self.ac = ActionChains(self._driver)

    def _click_and_hold(self, on_element, seconds):
        self.ac.click_and_hold(on_element).pause(seconds).release(on_element).perform()

    def _get_waiter(self, time):
        return WebDriverWait(self._driver, time)

    def _find_element(self, by: str, locator: str) -> WebElement:
        return self._driver.find_element(by, locator)

    def _find_elements(self, by, locator) -> List[WebElement]:
        return self._driver.find_elements(by, locator)

    def _click(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).click()

    def _click_after_time(self, by, locator, time):
        self._get_waiter(time).until(EC.visibility_of_element_located((by, locator)))
        return self._click(by, locator)

    def _send_keys(self, by, locator, text):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).clear()
        self._find_element(by, locator).send_keys(text)

    def scroll(self, x: int, y: int):
        return self._driver.execute_script(f'window.scroll({x}, {y})')

    # def foo(self, *args):
    #     print(type(args)) # list
        # print(*args) #

    def scroll_by_element(self, element: WebElement):
        # return self._driver.execute_script(f"document.querySelector('{selector}').scrollIntoView()")
        return self._driver.execute_script('arguments[0].scrollIntoView({block: "end", inline: "nearest"})', element)

