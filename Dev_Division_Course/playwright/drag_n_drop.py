from playwright.sync_api import sync_playwright
import time
# https://github.com/microsoft/pright/issues/1094


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    browser = browser.new_context(ignore_https_errors=True)
    page = browser.new_page()

    page.goto("https://cdpn.io/ThibaultJanBeyer/fullembedgrid/pNOWeq?animations=run&type=embed")
    frame_one = page.wait_for_selector("iframe").content_frame()
    coords = frame_one.locator('#element1').bounding_box()

    page.mouse.move(coords['x'], coords['y'])
    page.mouse.down()
    page.mouse.move(coords['x'] + 700, coords['y'])

    time.sleep(10)
