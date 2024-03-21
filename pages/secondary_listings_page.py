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
        # sleep(3)
        self.wait.until(EC.visibility_of_element_located(self.TOTAL_PAGE_BTN),
                        message=f'Could not find {self.TOTAL_PAGE_BTN} locator for {locator}')
        total_pages_count = self.driver.find_element(*self.TOTAL_PAGE_BTN).text

        for page in range(0,int(total_pages_count)):
            self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE_BTN),
                        message=f"Element by {locator} is not clickable"
                        ).click()

    def click_prev_page(self, *locator):
        self.wait.until(EC.visibility_of_element_located(self.CURRENT_PAGE_BTN),
                        message=f'Could not find {self.CURRENT_PAGE_BTN} locator for {locator}')
        total_pages_count = self.driver.find_element(*self.TOTAL_PAGE_BTN).text
        current_page_count = self.driver.find_element(*self.CURRENT_PAGE_BTN).text
        for page in range(int(total_pages_count),int(current_page_count),-1):
                self.wait.until(EC.element_to_be_clickable(self.PREV_PAGE_BTN),
                                message=f"Element by {locator} is not clickable"
                                ).click()



