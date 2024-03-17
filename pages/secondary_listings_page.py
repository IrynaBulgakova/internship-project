from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SecondaryListingsPage(Page):
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
    PREV_PAGE_BTN = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')
    TOTAL_PAGE_BTN = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    CURRENT_PAGE_BTN = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')

    def verify_correct_page_url(self):
        url = self.driver.current_url
        assert 'secondary-listings' in url, f'Expected "secondary-listings" not in {url}'

    def click_next_page(self, *locator):
        i = self.TOTAL_PAGE_BTN
        for i in range(1,58):
            if i != 59:
                self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE_BTN),
                        message=f"Element by {locator} is not clickable"
                        ).click()

    def click_prev_page(self, *locator):
        p = self.PREV_PAGE_BTN
        for p in range(1,58,-1):
            if p!= 1:
                self.wait.until(EC.element_to_be_clickable(self.PREV_PAGE_BTN),
                                message=f"Element by {locator} is not clickable"
                                ).click()










