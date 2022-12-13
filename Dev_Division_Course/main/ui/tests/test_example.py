import os

# https://chromedriver.chromium.org/
import time

import pytest
from uuid import uuid4
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest
@pytest.mark.debug
def test_foo(browser):
    browser.get('https://ya.ru')
    assert browser.current_url == 'https://ya.ru/'


@pytest.mark.skip
def test_slider(browser):
    # browser.implicitly_wait(12)

    wait = WebDriverWait(browser, 15)

    old_url = browser.current_url

    def wait_slider(driver):
        return driver.find_element(By.XPATH, "(//div[@class='slide-copy'])[2]//a").is_displayed()

    wait.until(wait_slider)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='slide-copy'])[2]//a"))
    )

    browser.find_element(By.XPATH, "(//div[@class='slide-copy'])[2]//a").click()
    time.sleep(1)
    assert old_url != browser.current_url


@pytest.mark.skip
def test_download(browser):
    browser.find_element(By.CSS_SELECTOR, '.download-for-current-os .download-buttons a').click()

    wait = WebDriverWait(browser, 10)

    files = os.listdir('/tmp')

    def wait_file(_):
        return len(files) < len(os.listdir('/tmp'))

    wait.until(wait_file)
    time.sleep(10)
