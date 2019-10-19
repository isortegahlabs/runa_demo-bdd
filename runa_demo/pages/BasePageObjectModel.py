from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObjectModel(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 35

    def wait_for_element_clickable(self, *locator):
        try:
            WebDriverWait(self.browser, 20, 1).until(EC.element_to_be_clickable(locator))
        except BaseException:
            print(u"%s no such %s element is found" % locator)
        else:
            return self.browser.find_element(*locator)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def refresh(self):
        self.browser.refresh()

    def get_text_element(self, *locator):
        return self.browser.find_element(*locator).text