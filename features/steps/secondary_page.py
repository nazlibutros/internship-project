from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify the secondary page opened')
def verify_main_page_opened(context):
    sleep(5)
    context.app.secondary_page.verify_secondary_page_opened()


@then('Click on Filters button')
def click_filters_button(context):
    context.app.secondary_page.click_filters()
    sleep(5)


@then('Filter the products by price range from {min_price} to {max_price}')
def filter_by_price(context, min_price, max_price):
    sleep(5)
    context.app.secondary_page.filter_by_price(min_price, max_price)


@then('Click on Apply filter button')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()
    sleep(5)


@then('Verify the price in all cards is inside the range ({min_price} - {max_price})')
def verify_prices_in_range(context, min_price, max_price):
    sleep(5)
    context.app.secondary_page.verify_prices_in_range(min_price, max_price)
