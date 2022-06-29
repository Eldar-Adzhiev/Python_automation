from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    driver = webdriver.Chrome()
    driver.get(link)

    # Считать значение для переменной x
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # Посчитать математическую функцию от x
    calculate = calc(x)

    # Ввести ответ в текстовое поле
    input_answer = driver.find_element(By.CSS_SELECTOR,"#answer")
    input_answer.send_keys(calculate)

    # Выбрать checkbox "I'm the robot"
    choose_checkbox = driver.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    choose_checkbox.click()

    # Переключить radiobutton "Robots rule!"
    choose_radiobutton = driver.find_element(By.CSS_SELECTOR,"#robotsRule")

    # Проскроллить страницу вниз
    driver.execute_script("return arguments[0].scrollIntoView(true);", choose_radiobutton)
    # Переключить radiobutton "Robots rule!
    choose_radiobutton.click()

    # Нажать на кнопку "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR,".btn")
    # driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()


finally:
    time.sleep(5)
    driver.quit()
