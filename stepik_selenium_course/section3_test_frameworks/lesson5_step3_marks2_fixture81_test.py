"""
Инверсия
Чтобы запустить все тесты, не имеющие заданную маркировку, можно
использовать инверсию. Для запуска всех тестов, не отмеченных как smoke,
нужно выполнить команду:

pytest -s -v -m "not smoke" lesson5_step3_marks2_fixture81_test.py

Объединение тестов с разными маркировками
Для запуска тестов с разными метками можно использовать логическое ИЛИ.
Запустим smoke и regression-тесты:

pytest -s -v -m "smoke or regression" lesson5_step3_marks2_fixture81_test.py

Выбор тестов, имеющих несколько маркировок
Предположим, у нас есть smoke-тесты, которые нужно запускать только для
определенной операционной системы, например, для Windows 10.
Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному
из тестов эту метку.

pytest.ini:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win10
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


"""
Чтобы запустить только smoke-тесты для Windows 10, нужно использовать 
логическое И:

pytest -s -v -m "smoke and win10" lesson5_step3_marks2_fixture81_test.py
Должен выполнится тест 
test_guest_should_see_basket_link_on_the_main_page. 
"""



