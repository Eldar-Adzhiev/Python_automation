from playwright.sync_api import sync_playwright
import time
# https://playwright.dev/python/docs/api/class-filechooser


with sync_playwright() as playwright:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    browser = browser.new_context(ignore_https_errors=True)
    page = browser.new_page()

    page.goto("https://ps.uci.edu/~franklin/doc/file_upload.html")
    with page.expect_file_chooser() as fc_info:
        time.sleep(5)
        page.click("[name='userfile']")

    file_chooser = fc_info.value
    file_chooser.set_files("/Users/akransov/PycharmProjects/CourseRepo/requirements.txt")
    page.click("[type='submit']")
    time.sleep(10)
