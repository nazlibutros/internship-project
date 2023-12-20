from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Log in page')
def open_login(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(5)


@when('Input {email} and {password}')
def input_credentials(context, email, password):
    context.app.signin_page.input_credentials(email, password)

@when('Click on Continue')
def click_continue(context):
    context.app.signin_page.click_continue()

