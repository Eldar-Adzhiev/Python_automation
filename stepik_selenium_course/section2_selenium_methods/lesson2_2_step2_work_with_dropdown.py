from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)


# browser.find_element(By.TAG_NAME, "select").click()
# browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

"""
Это не самый удобный способ, так как нам приходится делать лишний клик для
открытия списка.

Есть более удобный способ, для которого используется специальный класс Select 
из библиотеки WebDriver. Вначале мы должны инициализировать новый объект, 
передав в него WebElement с тегом select. Далее можно найти любой вариант из 
списка с помощью метода select_by_value(value):
"""
from selenium.webdriver.support.ui import Select

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")

"""
Можно использовать еще два метода: select.select_by_visible_text("text") и 
select.select_by_index(index). Первый способ ищет элемент по видимому тексту,
например, select.select_by_visible_text("Python") найдёт "Python" для нашего
примера.

Второй способ ищет элемент по его индексу или порядковому номеру. Индексация
начинается с нуля. Для того чтобы найти элемент с текстом "Python", нужно 
использовать select.select_by_index(1), так как опция с индексом 0 в данном 
примере имеет значение по умолчанию равное "--".
"""