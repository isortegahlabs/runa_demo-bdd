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
        "savepayroll_btn": (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/form/div[3]/button[2]'),
        "start_btn": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[4]/div/div[2]/div[2]/button'),
        "deletepayroll_btn": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/button/span'),
        "confirmdeletepayroll_btn": (By.XPATH, '/html/body/div[8]/div/div/div/div/button[2]'),
        "first_employee_txt": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                         '1]/table/tbody/tr[1]/td[2]'),
        "editsalaryoption_elm": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                           '1]/table/tbody/tr[2]/td[5]/div/div/div/span'),
        "editsalary_input": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                       '1]/table/tbody/tr[2]/td[5]/div[1]/div/div/div/input'),
        "savesalary_btn": (By.XPATH, '/html/body/div[1]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                     '1]/table/tbody/tr[2]/td[7]/button'),
        "third_employee_txt": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                         '1]/table/tbody/tr[5]/td[2]'),
        "deleteemployee_opt": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[2]/div[1]/div['
                                         '1]/table/tbody/tr[6]/td[2]/button/span'),
        "confirmdeleteemployee_btn": (By.XPATH, '/html/body/div[9]/div/div/div/div/button[2]'),
        "continue2_btn": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[3]/div/div[3]/button[2]'),
        "selectall_chk": (By.ID, 'selectMainCheckbox'),
        "sectioncalculate_elm": (By.XPATH, '//*[@id="root"]/div/div/div/div/section/div[2]/article[1]/h3/strong')
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
        time.sleep(4)

    def select_comenzar(self):
        self.find_element(*self.locator_map["start_btn"]).click()
        time.sleep(15)

    def open_detail_first_employee(self):
        self.find_element(*self.locator_map["first_employee_txt"]).click()

    def remove_payroll(self):
        self.find_element(*self.locator_map["deletepayroll_btn"]).click()

    def modify_salary(self, salary):
        self.find_element(*self.locator_map["editsalaryoption_elm"]).click()
        time.sleep(2)
        self.find_element(*self.locator_map["editsalary_input"]).send_keys(Keys.SHIFT
                                                                           + Keys.CONTROL + Keys.ARROW_LEFT)
        self.find_element(*self.locator_map["editsalary_input"]).send_keys(salary + Keys.ENTER)
        time.sleep(5)

    def save_employee_changes(self):
        self.find_element(*self.locator_map["savesalary_btn"]).click()
        time.sleep(3)

    def open_detail_third_employee(self):
        self.find_element(*self.locator_map["third_employee_txt"]).click()
        time.sleep(1)

    def delete_employee(self):
        self.find_element(*self.locator_map["deleteemployee_opt"]).click()
        time.sleep(3)

    def confirm_delete_employee(self):
        self.find_element(*self.locator_map["confirmdeleteemployee_btn"]).click()
        time.sleep(3)
        self.refresh()
        time.sleep(5)

    def continue_step_2(self):
        self.find_element(*self.locator_map["continue2_btn"]).click()

    def unselect_all(self):
        self.find_element(*self.locator_map["selectall_chk"]).click()
        time.sleep(1)

    def section_calculate(self):
        self.find_element(*self.locator_map["sectioncalculate_elm"]).click()
        time.sleep(1)

    def confirm_remove_payroll(self):
        self.find_element(*self.locator_map["confirmdeletepayroll_btn"]).click()

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