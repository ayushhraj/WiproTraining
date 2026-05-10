import allure
from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then

from pages.login_page import LoginPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger = LogGen.loggen()

@given(u'User launches application')
def step_impl(context):
    logger.info('Application URL loaded')


@when(u'User clicks on Login menu')
def step_impl(context):
    logger.info('Step : Click Login Menu')
    context.login_page = LoginPage(context.driver)
    context.login_page.click_login_menu()


@when(u'User enters valid username "{username}"')
def step_impl(context, username):
    logger.info(f"Step : Enter Valid Username : {username}")
    context.login_page.enter_username(username)


@when(u'User enters valid password "{password}"')
def step_impl(context, password):
    logger.info(f"Step : Enter Valid Password : {password}")
    context.login_page.enter_password(password)


@when(u'User enters username "{username}"')
def step_impl(context, username):
    logger.info(f"Step : Enter Username : {username}")
    context.login_page.enter_username(username)


@when(u'User enters password "{password}"')
def step_impl(context, password):
    logger.info(f"Step : Enter Password : {password}")
    context.login_page.enter_password(password)


@when(u'User clicks Login button')
def step_impl(context):
    logger.info("Step : Click Login Button")
    context.login_page.click_login_button()


@then(u'User should login successfully')
def step_impl(context):
    logger.info("Step : Verify Successful Login")
    context.login_page.verify_login_success()


@then(u'User should see login error message')
def step_impl(context):
    logger.info("Step : Verify Login Error Message")
    context.login_page.verify_login_error()


@then(u'User should see validation alert')
def step_impl(context):
    logger.info("Step : Verify Validation Alert")
    context.login_page.verify_validation_alert()


@when(u'User clicks Logout button')
def step_impl(context):
    logger.info("Step : Click Logout Button")
    context.login_page.click_logout_button()


@then(u'User should logout successfully')
def step_impl(context):
    logger.info("Step : Verify Successful Logout")
    context.login_page.verify_logout_success()
