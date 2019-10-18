from runa_demo.pages.BasePageObjectModel import BasePageObjectModel
from selenium.webdriver.common.by import By

import time


class LoginPage(BasePageObjectModel):

    locator_map = {
        "welcome_messaage": (By.CLASS_NAME, 'login-welcome-message'),
        "email": (By.ID, 'email'),
        "passwd": (By.ID, 'password'),
        "login_btn": (By.XPATH, '//*[@id="root"]/div/div/div/form/button')
    }

    def __init__(self, context):
        BasePageObjectModel.__init__(self, context.browser)

    def login(self, username, passwd):
        self.find_element(*self.locator_map['email']).send_keys(username)
        self.find_element(*self.locator_map['passwd']).send_keys(passwd)
        self.find_element(*self.locator_map['login_btn']).click()
        time.sleep(5)