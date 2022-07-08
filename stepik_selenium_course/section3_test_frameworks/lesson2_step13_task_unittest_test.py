from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# python -m unittest lesson2_step13_task_unittest_test.py



class TestUniqueSelectors(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def open_page(self, link):
        self.browser.get(link)

    def input_first_name(self, first_name: str):
        first_name_in = self.browser.find_element(By.CSS_SELECTOR, "div.first_block  .first")
        first_name_in.send_keys(first_name)

    def input_last_name(self, last_name: str):
        last_name_in = self.browser.find_element(By.CSS_SELECTOR, "div.first_block  .second")
        last_name_in.send_keys(last_name)

    def input_email(self, email: str):
        email_in = self.browser.find_element(By.CSS_SELECTOR, "div.first_block  .third")
        email_in.send_keys(email)

    def click_submit(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


    def test_login_registration1(self):
        self.open_page(link1)
        self.input_first_name("Eldar")
        self.input_last_name("Adzhiev")
        self.input_email("eldar@mail.ru")
        self.click_submit()
        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_login_registration2(self):
        self.open_page(link2)
        self.input_first_name("Eldar")
        self.input_last_name("Adzhiev")
        self.input_email("eldar@mail.ru")
        self.click_submit()
        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

