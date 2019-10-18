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
        "nominaGroup_input": (By.ID, 'react-select-payroll_group_id-input'),
        "selectStartDate_input": (By.ID, 'start_date'),
        "startDateIncidence_input": (By.ID, 'start_date_incidence'),
        "startMonth_txt": (By.XPATH, '/html/body/div[9]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong'),
        "backward_btn": (By.XPATH, '/html/body/div[9]/div/div/div/div/div[2]/div[1]/button[1]'),
        "startday": (By.XPATH, '/html/body/div[9]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[5]'),
        "endday": (By.XPATH, '/html/body/div[9]/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]'),
        "savepayroll_btn": (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/form/div[3]/button[2]')
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

    def select_date(self, date):
        self.find_element(*self.locator_map["selectStartDate_input"]).send_keys(date + Keys.ENTER)

    def select_range_incidents(self, startdate, enddate):
        self.find_element(*self.locator_map["startDateIncidence_input"]).click()
        self.__findMonth(startdate)
        time.sleep(1)
        self.find_element(*self.locator_map["startday"]).click()
        time.sleep(1)
        self.find_element(*self.locator_map["endday"]).click()
        time.sleep(1)
        self.find_element(*self.locator_map["savepayroll_btn"]).click()


    def __get_month(self, date):
        arraydate = date.split("/")
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                  "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return months[number.index(int(arraydate[1]))]

    def __findMonth(self, date):
        month = self.__get_month(date) + " " + date.split("/")[2]
        while month != self.find_element(*self.locator_map["startMonth_txt"]).text:
            self.find_element(*self.locator_map["backward_btn"]).click()
            time.sleep(1)