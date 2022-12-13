import time

# from selenium.webdriver import ActionChains, TouchActions

import pytest
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

# https://www.w3.org/TR/webdriver/
# https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.touch_actions.html


# @pytest.mark.debug
def test_mobile(browser):
    browser.get('https://go.mail.ru/msearch?q=%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80+2&src=mgo&mobile_result=Smartphone&frm=main&fr=main&sbmt=1649623514508/')
    # ac = ActionChains(browser)
    # tc = TouchActions(browser)
    browser.execute_script('arguments[0].scrollIntoView()', browser.find_elements(By.CSS_SELECTOR, '.ObjectSnippet-person')[0])
    time.sleep(1)
    # print([True for el in browser.find_elements(By.CSS_SELECTOR, '.ObjectSnippet-person') if el.is_displayed()])

    for position in range(2, 5):
        el = browser.find_element(By.XPATH, f"(//*[contains(@class, 'ObjectSnippet-person')])[{position}]")

        ac = ActionBuilder(browser, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # ac.pointer_action.move_to_location(el.rect['x'] + el.rect['width'], el.rect['y'])
        ac.pointer_action.move_to(el, 0, 0)
        ac.pointer_action.pointer_down()
        ac.pointer_action.pause(2)
        # ac.pointer_action.move_to_location((el.rect['x'] - el.rect['width'] / 2), el.rect['y'])
        ac.pointer_action.move_to(el, -60, 0)
        ac.pointer_action.release()
        # actions.perform()
        ac.perform()
        time.sleep(2)

    # print([True for el in browser.find_elements(By.CSS_SELECTOR, '.ObjectSnippet-person') if el.is_displayed()])

    time.sleep(10)
