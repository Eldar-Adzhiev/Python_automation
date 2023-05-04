from playwright.sync_api import Page

from playwright_practices.example_ui_auto.pages.base_page import BasePage


class PlaywrightHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)