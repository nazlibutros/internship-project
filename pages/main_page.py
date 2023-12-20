from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SECONDARY = (By.CSS_SELECTOR, "[class='menu-button-block link-block link-block-2 link-block-3 link-block-4 "
                                  "w-inline-block']")

    def verify_main_page_opened(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("https://soft.reelly.io/"))
        sleep(10)

    def click_secondary_option(self):
        self.driver.find_element(*self.SECONDARY).click()
