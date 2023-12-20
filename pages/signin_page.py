from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SigninPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")

    def input_credentials(self, email, password):
        print('input_credentials')
        print(email)
        print(password)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

