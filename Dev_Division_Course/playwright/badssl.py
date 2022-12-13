from playwright.sync_api import sync_playwright
import time


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    browser = browser.new_context(ignore_https_errors=True)
    # browser.grant_permissions()
    page = browser.new_page()
    page.goto("https://expired.badssl.com/")
    time.sleep(2)
    browser.close()
