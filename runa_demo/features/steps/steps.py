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


@when(u'we visit the site')
def step_visit_site(context):
    context.browser.get(context.urlBase)


@when(u'we wait for the "{element}" element')
def step_wait_for_visibility(context, element):
    context.element = element
    loginpage = LoginPage(context)
    loginpage.wait_for_element_clickable(*loginpage.locator_map[element])


@when(u'we make login successful')
def step_login(context):
    loginpage = LoginPage(context)
    loginpage.login(context.username, context.password)


@when(u'we wait for the "{element}" element of modal')
def step_wait_for_visibility(context, element):
    nominapage = NominaPage(context)
    nominapage.wait_for_element_clickable(*nominapage.locator_map[element])


@when(u'we close the modal for change the password')
def step_close_modal_change_password(context):
    nominapage = NominaPage(context)
    nominapage.close_modal_change_password()


@when(u'we create a new nomina manual')
def step_createnomina(context):
    nominapage = NominaPage(context)
    nominapage.new_nomina()


@when(u'we are looking for the payroll group "{group}"')
def step_search_nomina_group(context, group):
    nominapage = NominaPage(context)
    nominapage.search_nomina_group(group)


@then('')
def simpl_step(context):
    pass


@step('')
def simpl_step(context):
    pass
