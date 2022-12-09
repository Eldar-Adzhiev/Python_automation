import pytest

from ..framework.browser.browser import Browser
from .tests.config.browser import Grid


@pytest.fixture(scope="function", autouse=True)
def browser():
    browser = Browser()
    browser.set_up_driver(is_incognito=True, enable_performance_logging=True)
    browser.maximize()
    browser.set_url(Grid.GRID_URL)

    yield browser

    browser.quit()
