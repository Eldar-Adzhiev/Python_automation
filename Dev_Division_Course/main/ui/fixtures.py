import os

import allure
import pytest
# Подключение прокси
# from selenium.webdriver import Proxy
# from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# https://expired.badssl.com/
# https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView -- скролл
# https://ps.uci.edu/~franklin/doc/file_upload.html -- для загрузки файлов
# https://thibaultjanbeyer.github.io/dragNdrop/#twob -- dragndrop/iframe
# https://cdpn.io/ThibaultJanBeyer/fullembedgrid/RoYZRb?animations=run&type=embed -- iframe + dragndrop
# https://cdpn.io/ThibaultJanBeyer/fullembedgrid/pNOWeq?animations=run&type=embed -- iframe + dragndrop to el
# https://cdpn.io/aikrasnov/fullpage/WNdNWrP -- disabled input
# https://cdpn.io/ralzohairi/fullembedgrid/JgMvNg?animations=run&type=embed -- broken hk
# https://cdpn.io/code-boxx/fullpage/RwjdZBg tooltip
# https://chromedevtools.github.io/devtools-protocol/
# https://www.selenium.dev/documentation/webdriver/bidirectional/chrome_devtools/
# https://docs.qameta.io/allure/#_installing_a_commandline -- allure

# selenoid
# https://aerokube.com/selenoid/latest/ -- doc
# https://aerokube.com/cm/latest/ -- quick start guide and configuration manager
# https://github.com/aerokube/cm/releases/tag/1.8.1 -- latest CM release
# https://hub.docker.com/r/selenoid/chrome/tags -- main selenoid hub with docker images

# https://playwright.dev/



@pytest.fixture(scope='session')
def ui_config(request):
    if request.config.getoption('--selenoid'):
        selenoid = 'http://selenoid:4444'
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False

    else:
        selenoid = None
        vnc = False

    return {'selenoid': selenoid, 'vnc': vnc}


@pytest.fixture(scope='function')
def browser(request, test_dir, ui_config):
    selenoid = ui_config['selenoid']
    vnc = ui_config['vnc']

    options = ChromeOptions()
    # mobile_emulation = {"deviceName": "Pixel 5"}
    # mobile_emulation = {"deviceName": "Samsung Galaxy S20 Ultra"}
    # mobile_emulation = {"deviceName": "iPhone SE"}
    mobile_emulation = {
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 1.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"  # NOQA
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    # https://www.w3.org/TR/webdriver/
    # options.add_experimental_option('w3c', False)

    prefs = {}
    if not selenoid:
        prefs['download.default_directory'] = test_dir

    # Установка гео для профиля:
    # prefs = {
    #     'profile.default_content_setting_values':
    #         {
    #             'notifications': 1,
    #             'geolocation': 1
    #         },
    #     'devtools.preferences': {
    #         'emulation.geolocationOverride': "\"11.111698@-122.222954:\"",
    #     },
    #     'profile.content_settings.exceptions.geolocation': {
    #         'BaseUrls.Root.AbsoluteUri': {
    #             'last_modified': '13160237885099795',
    #             'setting': '1'
    #         }
    #     },
    #     'profile.geolocation.default_content_setting': 1
    #
    # }

    # Запуск мокера-прокси
    # docker run -p 1080:1080 --name proxy -d mockserver/mockserver
    # http://localhost:1080/mockserver/dashboard
    # https://mock-server.com/
    options.add_experimental_option("prefs", prefs)
    # Подключение прокси и расслабление безопасности
    # options.add_argument('--proxy-server=localhost:1080')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--ignore-certificate-errors')

    # Подключение прокси
    # proxy = Proxy({
    #     'proxyType': 'manual',
    #     'httpProxy': 'localhost:1080',
    #     'sslProxy': 'localhost:1080',
    # })

    # caps = {}
    # proxy.add_to_capabilities(caps)
    #
    # options.set_capability('proxy', caps)
    # options.set_capability('proxy', {
    #     'proxyType': 'manual',
    #     'httpProxy': 'localhost:1080',
    #     'sslProxy': 'localhost:1080',
    # })

    if selenoid is not None:
        capabilities = {
            'browserName': 'chrome',
        }
        if vnc:
            capabilities['version'] += '_vnc'
            capabilities['enableVNC'] = True

        driver = Remote(selenoid + '/wd/hub', options=options, desired_capabilities=capabilities)
    else:
        manager = ChromeDriverManager(log_level=0)
        path = manager.install()

        service = Service(executable_path=path)
        driver = Chrome(service=service, options=options)

    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = os.path.join(test_dir, 'failure.png')
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_log_path = os.path.join(test_dir, 'browser.log')
        with open(browser_log_path, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_log_path, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    driver.quit()
