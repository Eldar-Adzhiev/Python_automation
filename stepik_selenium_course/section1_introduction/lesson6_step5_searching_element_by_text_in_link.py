"""
В этой задаче мы попробуем искать элементы по тексту ссылки, для этого воспользуемся методом find_element_by_link_text:

link = browser.find_element(By.LINK_TEXT, text)
В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. Это тот самый текст, который
содержится между открывающим и закрывающим тегом <a> вот тут </a>

Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти
по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код:

link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()
А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:

link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()
Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что находится
нужный элемент
"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e)*10000))

    link_text = browser.find_element(By.LINK_TEXT, text)
    link_text.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()




