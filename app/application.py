from pages.base_page import Page
from pages.main_page import MainPage
from pages.signin_page import SigninPage
from pages.secondary_page import SecondaryPage


class Application:
    def __init__(self, driver):
        """

        :type driver: object
        """
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SigninPage(driver)
        self.secondary_page = SecondaryPage(driver)

