import os

import allure
import pytest
import time
import requests

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from main.ui.page_object.simple.mainpage import MainPage, DescrMainPage
from main.ui.suite.base import BaseUISuiteTest
import json

from utils.decorators import wait


class TestMainPageUI(BaseUISuiteTest):

    @pytest.mark.skip
    def test_search_mail_ru(self):
        # docker run -p 1080:1080 --name proxy -d mockserver/mockserver
        print(requests.put('http://localhost:1080/clear').content)
        self.browser.get('https://go.mail.ru')
        # time.sleep(1)
        with open('result', 'w') as fp:
            resp = requests.put('http://localhost:1080/mockserver/retrieve?type=REQUEST_RESPONSES').json()
            fp.write(json.dumps(resp))

    @pytest.mark.skip
    def test_cdp_geolocation(self):
        params = {
            "latitude": 35.1408845,
            "longitude": -62.5033907,
            "accuracy": 100
        }
        # https://chromedevtools.github.io/devtools-protocol/
        self.browser.execute_cdp_cmd("Emulation.setScrollbarsHidden", {"hidden": True})
        self.browser.get("https://yandex.ru")
        time.sleep(1)
        self.browser.set_window_size(500, 400)
        time.sleep(1)
        # self.browser.execute_cdp_cmd()
        self.browser.execute_script(f'window.scroll(9999, 9999)')
        time.sleep(10)

        # element = WebDriverWait(self.browser, 20).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='mylocation']")))  # added
        # element.click()
        # time.sleep(10)

    @pytest.mark.skip
    def test_rel_locators(self):
        self.browser.get('https://www.python.org/')
        self.browser.maximize_window()
        time.sleep(1)
        el1 = self.browser.find_element(By.CSS_SELECTOR, ".icon-search+label")
        el2 = self.browser.find_element(By.CSS_SELECTOR, "button.search-button")
        el3 = self.browser.find_element(By.CSS_SELECTOR, ".options-bar")
        # Use tag name and relative locators to find the web elements between them
        elements = self.browser.find_elements(
            # .icon-search+label > .icon-search > input
            locate_with(By.CSS_SELECTOR, '#site-map-link')
                .above(el3)
        )
        time.sleep(1)
        print('\n\n\n')
        print(elements)
        print(elements[0].get_attribute('href'))
        print('\n\n\n')
        time.sleep(1)

    @pytest.fixture()
    def upload_file_path(self, repo_root):
        return os.path.join(repo_root, "ui/page_object/simple/page.py")

    def test_upload_file(self, upload_file_path):
        self.browser.get('https://ps.uci.edu/~franklin/doc/file_upload.html')
        self.browser.find_element(By.CSS_SELECTOR, "[name='userfile']").send_keys(upload_file_path)
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(5)

    @allure.step('Checking download')
    def check_download(self, file_name, test_dir):
        if selenoid := self.ui_config['selenoid']:
            res = requests.get(f'{selenoid}/download/{self.browser.session_id}/{file_name}')
            if res.status_code == 404:
                return False

            with open(os.path.join(test_dir, file_name), 'wb') as f:
                f.write(res.content)
            return True

        else:
            for f in os.listdir(test_dir):
                if f.endswith('.crdownload'):
                    return False

            assert file_name in os.listdir(test_dir)
            return True

    def test_download(self, browser, test_dir):
        from selenium.webdriver.common.by import By
        browser.get('https://www.python.org/downloads/release/python-2717/')

        file_name = 'python-2.7.17.amd64-pdb.zip'
        browser.find_element(By.XPATH, f'//a[contains(@href, "{file_name}")]').click()

        wait(self.check_download, error=AssertionError, timeout=15, interval=0.1, check=True, file_name=file_name,
             test_dir=test_dir)

    def test_get_n_change_input(self):
        self.browser.get('https://cdpn.io/aikrasnov/fullpage/WNdNWrP')
        time.sleep(3)
        self.browser.switch_to.frame(self.browser.find_element(By.CSS_SELECTOR, 'iframe'))
        # print('input text is (by text): ', self.browser.find_element(By.XPATH, '//input[2]').text)
        # print('input text is (by text): ', self.browser.find_element(By.XPATH, '//input[2]').get_attribute('value'))
        # self.browser.find_element(By.XPATH, '//input[2]').send_keys('foobar')
        self.browser.execute_script('arguments[0].value="foobar"', self.browser.find_element(By.XPATH, '//input[2]'))
        time.sleep(3)

    def test_drag_n_drop(self):
        self.browser.get('https://cdpn.io/ThibaultJanBeyer/fullembedgrid/pNOWeq?animations=run&type=embed')

        self.browser.switch_to.frame(
            self.browser.find_element(By.CSS_SELECTOR, 'iframe')
        )
        ac = ActionChains(self.browser)
        el1 = self.browser.find_element(By.CSS_SELECTOR, '#element1')
        # drop_zone_1 = self.browser.find_element(By.CSS_SELECTOR, '#dropZone1')
        ac.drag_and_drop_by_offset(el1, xoffset=100, yoffset=0).pause(1).drag_and_drop_by_offset(
            el1, xoffset=100, yoffset=0
        ).perform()
        time.sleep(3)

        self.browser.switch_to.parent_frame()

    def test_scroll_by_element(self):
        main_page = self.get_page(MainPage)
        time.sleep(3)
        main_page.scroll_by_element(main_page.get_click_these())
        time.sleep(3)

    def test_scroll(self):
        main_page = self.get_page(MainPage)
        time.sleep(3)
        main_page.scroll(9999, 9999)
        time.sleep(3)
        main_page.scroll(-9999, -9999)
        time.sleep(3)

    def test_go_another_page(self):
        main_page = self.get_page(MainPage)
        assert 0
        time.sleep(10)
        d_page = main_page.go_to_downloads()
        assert d_page.is_page_loaded(), f'Страница {d_page.path} не загрузилась'
        assert d_page.get_widget_title_text() == 'Active Python Releases', 'Неправильный тайтл'

    @pytest.mark.parametrize('text', [
        'python',
        'python3'
    ])
    def test_search(self, text):
        page = self.get_page(MainPage)
        page.search_by_text(text)
        time.sleep(1)
        page.search_by_text('\n')
        time.sleep(1)
        assert 'python' in self.browser.page_source

    @pytest.mark.parametrize('text', [
        'python',
        'python3'
    ])
    def test_search_by_descr(self, text):
        page = self.get_page(DescrMainPage)

        page.search_input.send_keys(text)
        time.sleep(1)
        page.search_input.send_keys('\n')
        time.sleep(1)

        assert 'python' in self.browser.page_source


class TestLogUI(BaseUISuiteTest):

    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Log tests')
    @allure.testcase('Python events')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.issue('https://jira.vk.team/ISSUE-123')
    @allure.description("""We just go to python.org, then we go to events, then we go to PyConTW 2021 and then check
    it's location. Hmmm... Sounds good. Lois.
        """)
    @pytest.mark.smoke
    def test_browser_log(self):
        self.logger.info('STARTING TEST')

        with allure.step('Going to target.my.com'):
            self.browser.get('https://target.my.com')

        with allure.step('Checking assert 0'):
            with allure.step('Logging string'):
                self.logger.info('GOT URL')
            assert 0

    @allure.title('Main title')
    @allure.epic('Awesome PyTest framework')
    @allure.feature('UI tests')
    @allure.story('Log 2')
    def test_log2(self, test_dir):
        """some description"""
        allure.dynamic.feature(test_dir)
