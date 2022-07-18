from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how_search, what_search):
        try:
            self.browser.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True
