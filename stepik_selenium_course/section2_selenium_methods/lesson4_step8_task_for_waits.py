from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until \
        (EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    # Решить уже известную нам математическую задачу
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    calculate = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calculate)

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
