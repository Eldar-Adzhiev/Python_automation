from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    calculate = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calculate)

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

    # Скопировать ответ с Алерта  и принять его
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    alert.accept()


finally:
    time.sleep(15)
    browser.quit()



