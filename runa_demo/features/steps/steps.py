from behave import given, then, when, step
from runa_demo.pages.LoginPage import LoginPage
from runa_demo.pages.NominaPage import NominaPage
import time


@given(u'the URL "{urlBase}"')
def step_set_url_base(context, urlBase):
    context.urlBase = urlBase


@given(u'the username "{username}" and the password "{password}"')
def step_set_username_and_password(context, username, password):
    context.username = username
    context.password = password


@when(u'visit the site')
def step_visit_site(context):
    context.browser.get(context.urlBase)


@when(u'wait for the "{element}" element')
def step_wait_for_visibility(context, element):
    context.element = element
    loginpage = LoginPage(context)
    loginpage.wait_for_element_clickable(*loginpage.locator_map[element])

@when(u'wait for the "{element}" element in nomina page')
def step_wait_for_visibility(context, element):
    context.element = element
    nominapage = NominaPage(context)
    nominapage.wait_for_element_clickable(*nominapage.locator_map[element])

@when(u'make login successful')
def step_login(context):
    loginpage = LoginPage(context)
    loginpage.login(context.username, context.password)


@when(u'wait for the "{element}" element of modal')
def step_wait_element_clickable(context, element):
    nominapage = NominaPage(context)
    nominapage.wait_for_element_clickable(*nominapage.locator_map[element])


@when(u'close the modal for change the password')
def step_close_modal_change_password(context):
    nominapage = NominaPage(context)
    nominapage.close_modal_change_password()


@when(u'create a new nomina manual')
def step_createnomina(context):
    nominapage = NominaPage(context)
    nominapage.new_nomina()


@when(u'looking for the payroll group "{group}"')
def step_search_nomina_group(context, group):
    nominapage = NominaPage(context)
    nominapage.search_nomina_group(group)


@when(u'select day "{date}"')
def step_select_date(context, date):
    nominapage = NominaPage(context)
    nominapage.select_date(date)


@when(u'select range of incidents "{start}" to "{end}"')
def step_select_range_incidents(context, start, end):
    nominapage = NominaPage(context)
    nominapage.select_range_incidents(start, end)


@when(u'select option comenzar')
def step_select_comenzar(context):
    nominapage = NominaPage(context)
    nominapage.select_comenzar()


@when(u'open the detail of the first employee')
def step_open_detail(context):
    nominapage = NominaPage(context)
    nominapage.open_detail_first_employee()


@when(u'modify the salary field with "{salary}" pesos')
def step_modify_salary(context, salary):
    nominapage = NominaPage(context)
    nominapage.modify_salary(salary)


@when(u'remove payroll')
def step_select_comenzar(context):
    nominapage = NominaPage(context)
    nominapage.remove_payroll()


@when(u'confirm delete payroll')
def step_select_comenzar(context):
    nominapage = NominaPage(context)
    nominapage.confirm_remove_payroll()
    time.sleep(5)


@when(u'save employee changes')
def step_save_employee_changes(context):
    nominapage = NominaPage(context)
    nominapage.save_employee_changes()


@when(u'open the detail of the third employee')
def step_open_third_employee(context):
    nominapage = NominaPage(context)
    nominapage.open_detail_third_employee()


@when(u'delete payroll employee')
def step_delete_payroll_employee(context):
    nominapage = NominaPage(context)
    nominapage.delete_employee()


@when(u'confirm delete payroll employee')
def step_confirm_delete_payroll_employee(context):
    nominapage = NominaPage(context)
    nominapage.confirm_delete_employee()


@when(u'continue step {step}')
def step_continue_step_2(context, step):
    nominapage = NominaPage(context)
    nominapage.continue_step_2()

@when(u'unselect all')
def step_unselect_all(context):
    nominapage = NominaPage(context)
    nominapage.unselect_all()


@when(u'select option ADMINISTRADOR')
def step_section_calculate(context):
    nominapage = NominaPage(context)
    nominapage.select_admin_menu()


@when(u'select option CERRAR SESION')
def step_section_close(context):
    nominapage = NominaPage(context)
    nominapage.close_session()


@when(u'select section calculate')
def step_section_calculate(context):
    nominapage = NominaPage(context)
    nominapage.section_calculate()


@then(u'the login page is seen')
def step_assert_login_page(context):
    loginpage = LoginPage(context)
    assert "¡Te ves radiante hoy!" in loginpage.get_text_element(*loginpage.locator_map["welcome_messaage"])


@then(u'the login was successful')
def step_assert_login_success(context):
    loginpage = LoginPage(context)
    assert "Por seguridad actualiza tu contraseña" in loginpage.get_text_element(*loginpage.locator_map["change_modal_password_title"])


@then(u'payroll creation was successful')
def step_assert_payroll_create(context):
    nominapage = NominaPage(context)
    assert "Nómina Semanal Automation" in \
           nominapage.get_text_element(*nominapage.locator_map["assertpayrollname"])


@then(u'the new salary is $5,000.00')
def step_assert_edit_salary(context):
    nominapage = NominaPage(context)
    assert "$5,000.00" in \
           nominapage.get_text_element(*nominapage.locator_map["assertsalaryfirstemployee"])

@then(u'only 4 employees left')
def step_assert_employees(context):
    nominapage = NominaPage(context)
    assert 8 == nominapage.count_elements("assertcountemployees")