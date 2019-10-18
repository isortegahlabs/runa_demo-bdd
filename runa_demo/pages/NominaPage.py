from runa_demo.pages.BasePageObjectModel import BasePageObjectModel
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class NominaPage(BasePageObjectModel):

    locator_map = {
        "closeModal_btn": (By.CLASS_NAME, 'modal-close-icon'),
        "closeVideo_btn": (By.CLASS_NAME, 'video-close-icon'),
        "nomina_mnu": (By.XPATH, '//*[@id="root"]/div/div/aside/ul/li[3]/a/span'),
        "newNomina_btn": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/nav[2]/button'),
        "nominaGroup_input": (By.ID, 'react-select-payroll_group_id-input')
    }

    def __init__(self, context):
        BasePageObjectModel.__init__(self, context.browser)

    def close_modal_change_password(self):
        try:
            self.find_element(*self.locator_map["closeModal_btn"]).click()
        except BaseException:
            print("No such %s" % self.locator_map["closeModal_btn"][1])

    def new_nomina(self):
        self.find_element(*self.locator_map["nomina_mnu"]).click()
        self.find_element(*self.locator_map["closeVideo_btn"]).click()
        self.find_element(*self.locator_map["newNomina_btn"]).click()

    def search_nomina_group(self, group):
        self.find_element(*self.locator_map["nominaGroup_input"]).send_keys(group + Keys.ENTER)
        time.sleep(2)
