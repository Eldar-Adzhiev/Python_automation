from playwright.sync_api import sync_playwright
import time
# https://playwright.dev/python/docs/emulation#permissions
# Security & Privacy


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    browser = browser.new_context(ignore_https_errors=True, geolocation={"longitude": 48.858455, "latitude": 2.294474})
    # browser = browser.new_context(ignore_https_errors=True)
    browser.grant_permissions(['geolocation'], origin='https://www.google.ru')
    page = browser.new_page()

    page.goto("https://www.google.ru/maps/")
    time.sleep(10)
