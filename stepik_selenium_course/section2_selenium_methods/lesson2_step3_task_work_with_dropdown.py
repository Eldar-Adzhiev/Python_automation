from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем первый элемент
    el_1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    print(el_1)

    # Ищем второй элемент
    el_2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print(el_2)

    # Забираем значенияэлементов и переводим их в int
    sum = int(el_1) + int(el_2)
    print(sum)

    # Открываем дропдаун и выбираем нужный элемент
    select_sum = Select(browser.find_element(By.TAG_NAME, "select"))
    select_sum.select_by_value(str(sum))

    # Кликаем по кнопке
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

