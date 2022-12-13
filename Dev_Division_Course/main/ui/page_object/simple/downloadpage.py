from main.ui.page_object.simple.page import BasePage
from selenium.webdriver.common.by import By


class DownloadsPage(BasePage):
    """
        PageObject: https://www.python.org/downloads/.
    """

    path = '/downloads'

    WIDGET_ELEMENT = (By.CSS_SELECTOR, '.widget-title')

    def is_page_loaded(self) -> bool:
        assert self.path in self._driver.current_url
        return True

    def get_widget_title_text(self):
        return self._find_element(*self.WIDGET_ELEMENT).text
