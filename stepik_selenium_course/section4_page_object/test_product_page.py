import time
from pages.product_page import ProductPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button() #нажимаем кнопку добавления
    page.solve_quiz_and_get_code() #считаем функцию и копируем сообщение в alert_text
    time.sleep(5)
    page.should_be_correct_name_in_basket()  #проверяем имя товара и в корзине
    page.should_be_correct_price_in_basket() #проверяем цену товара и в корзине



