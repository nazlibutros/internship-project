from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify main page opened')
def verify_main_page_opened(context):
    context.app.main_page.verify_main_page_opened()


@when('Click on Secondary option at the left side menu')
def click_secondary(context):
    context.app.main_page.click_secondary_option()
    sleep(5)
