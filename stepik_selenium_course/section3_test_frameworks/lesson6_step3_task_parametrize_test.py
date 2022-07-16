import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


final_text = " "
@pytest.fixture(scope="function")
def browser():
    print("start browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("quit browser..")
    browser.quit()
    print(final_text)

@pytest.mark.parametrize("number", ["236895", "236896", "236897", "236898",
                                    "236899", "236903", "236904", "236905"])
def test_link(browser, number):
    global final_text
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    input_answer = browser.find_element(By.CLASS_NAME, "ember-text-area")
    input_answer.send_keys(answer)

    click_submit = browser.find_element(By.CLASS_NAME, "submit-submission")
    click_submit.click()

    check_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

    try:
        assert check_text == "Correct!", f"Текст = {check_text}, должно быть = Correct!"
    except AssertionError:
        final_text += check_text


