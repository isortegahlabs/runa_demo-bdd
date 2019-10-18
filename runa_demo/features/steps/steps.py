from behave import given, then, when, step
from runa_demo.pages.LoginPage import LoginPage
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
    # try:
    #     wait = WebDriverWait(context.browser, 10, 1)
    #     element = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    # except BaseException:
    #     print("algo")
    # else:
    #     context.browser.find_element(By.ID, 'email').clear()


@when(u'we make login successful')
def step_login(context):
    loginpage = LoginPage(context)
    loginpage.login(context.username, context.password)

@then('')
def simpl_step(context):
    pass


@step('')
def simpl_step(context):
    pass
