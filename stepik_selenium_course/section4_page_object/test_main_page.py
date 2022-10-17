import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        """
        Первый способ: возвращать нужный Page Object.
        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        login_page = page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_should_see_login_page(browser):
        """
        Второй подход: переход происходит неявно, страницу инициализируем в теле теста
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()
