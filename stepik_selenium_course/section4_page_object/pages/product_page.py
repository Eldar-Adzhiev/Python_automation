from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_name_in_basket(self):
        product_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(product_basket_name.text)
        print(product_name.text)
        assert product_basket_name.text == product_name.text, "Incorrect book name in basket"

    def should_be_correct_price_in_basket(self):
        product_basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        print(product_basket_price.text)
        print(product_price.text)
        assert product_price.text == product_basket_price.text, "Incorrect book price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disapper_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"