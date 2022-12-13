from playwright.sync_api import sync_playwright
import time


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://yandex.ru")
    time.sleep(2)
    browser.close()

