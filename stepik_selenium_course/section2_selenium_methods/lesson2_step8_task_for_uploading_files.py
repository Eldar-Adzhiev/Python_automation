import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"

with open("test.txt", "w") as file:
    file.write("Test creating file and uploud it")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.NAME, "firstname")
    input_first_name.send_keys("sdfdf")

    input_last_name = browser.find_element(By.NAME, "lastname")
    input_last_name.send_keys("sdfdf")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("sdfdf@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
