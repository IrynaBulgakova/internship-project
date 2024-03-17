from pages.base_page import Page
from pages.main_page import MainPage
from pages.secondary_listings_page import SecondaryListingsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.secondary_listings_page = SecondaryListingsPage(driver)
