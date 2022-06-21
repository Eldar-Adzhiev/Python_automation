"""
На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в
нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать в
коде именно на неё.

Ваши шаги:

В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как
угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.
Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве ответа
на это задание.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:

    driver = webdriver.Chrome()
    driver.get(link)

    input_first_name = driver.find_element(By.XPATH, "//input[@name='first_name']")
    input_first_name.send_keys("Ivan")

    input_last_name = driver.find_element(By.XPATH, "//input[@name='last_name']")
    input_last_name.send_keys("Petrov")

    input_city = driver.find_element(By.XPATH, "//input[@class='form-control city']")
    input_city.send_keys("Smolensk")

    input_country = driver.find_element(By.XPATH, "//input[@id='country']")
    input_country.send_keys("Russia")

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()



