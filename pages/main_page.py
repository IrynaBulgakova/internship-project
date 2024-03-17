from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD_INPUT = (By.CSS_SELECTOR, '[data-name="Password"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[wized="loginButton"]')
    SECONDARY_LISTINGS_BTN = (By.CSS_SELECTOR, '[href="/secondary-listings"]')

    def open_main_page(self):
        self.open('https://soft.reelly.io/')
        sleep(3)

    def log_in_email(self, text, *locator):
        # text = 'irynablv@gmail.com'
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(text)

    def log_in_password(self, text, *locator):
        # text = 'rumorhasit'
        self.driver.find_element(*self.PASSWORD_FIELD_INPUT).send_keys(text)

    def click_continue_btn(self, *locator):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def click_secondary_listings_option(self, *locator):
        self.driver.find_element(*self.SECONDARY_LISTINGS_BTN).click()
