from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.base_page import Page
from time import sleep


class SecondaryPage(Page):
    FILTERS_BUTTON = (By.CSS_SELECTOR, "[class*='filter-button']")
    APPLY_FILTERS_BUTTON = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, "[wized = 'unitPriceFromFilter']")
    FILTER_PRICE_TO = (By.CSS_SELECTOR, "[wized = 'unitPriceToFilter']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "[class ='number-price-text']")

    def verify_secondary_page_opened(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("https://soft.reelly.io/secondary-listings"))
        sleep(10)

    def click_filters(self):
        self.driver.find_element(*self.FILTERS_BUTTON).click()

    def filter_by_price(self, price_from, price_to):
        self.driver.find_element(*self.FILTER_PRICE_FROM).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.FILTER_PRICE_FROM).send_keys(price_from)

        self.driver.find_element(*self.FILTER_PRICE_TO).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.FILTER_PRICE_TO).send_keys(price_to)

    def click_apply_filter(self):
        self.driver.find_element(*self.APPLY_FILTERS_BUTTON).click()

    def verify_prices_in_range(self, min_price, max_price):
        product_prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        min_price = int(min_price)
        max_price = int(max_price)

        for price_element in product_prices:
            price = int(price_element.text.replace("AED", "").replace(",", "").strip())
            assert min_price <= price <= max_price, f"Price {price} is not in the expected range."
