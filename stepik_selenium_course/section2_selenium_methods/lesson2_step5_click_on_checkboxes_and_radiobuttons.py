from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(url)

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    calculate = calc(x)

    input_answer = driver.find_element(By.CSS_SELECTOR,"#answer")
    input_answer.send_keys(calculate)

    choose_checkbox = driver.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    choose_checkbox.click()

    choose_radiobutton = driver.find_element(By.CSS_SELECTOR,"#robotsRule")
    choose_radiobutton.click()

    submit_button = driver.find_element(By.CSS_SELECTOR,".btn")
    submit_button.click()


finally:
    time.sleep(5)
    driver.quit()


