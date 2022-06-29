from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    # 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    treasure_value = browser.find_element(By.CSS_SELECTOR, "#treasure")

    # 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = treasure_value.get_attribute("valuex")

    # 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
    calculate = calc(x)

    # 5. Ввести ответ в текстовое поле.
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calculate)

    # 6. Отметить checkbox "I'm the robot".
    choose_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    choose_checkbox.click()

    # 7. Выбрать radiobutton "Robots rule!".
    choose_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    choose_radiobutton.click()

    # 8. Нажать на кнопку "Submit".
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()




