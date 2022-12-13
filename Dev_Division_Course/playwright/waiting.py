from playwright.sync_api import sync_playwright
import time
# https://playwright.dev/docs/selectors
# https://playwright.dev/python/docs/actionability


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    browser = browser.new_context(ignore_https_errors=True)
    page = browser.new_page()

    search = 'foo'

    page.goto("https://python.org")
    page.click('#id-search-field')
    page.keyboard.type(search)
    page.click('#submit')
    assert search in page.text_content('.list-recent-events.menu li p')
    browser.close()
