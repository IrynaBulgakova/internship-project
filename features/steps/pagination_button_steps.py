from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Reelly.io')
def open_reelly_page(context):
    context.app.main_page.open_main_page()


@given('Log in to the main page')
def login(context):
    context.app.main_page.log_in_email(text='irynablgv@gmail.com')
    context.app.main_page.log_in_password(text='rumorhasit')
    context.app.main_page.click_continue_btn()


@when('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.main_page.click_secondary_listings_option()


@then('Verify the right page opens')
def verify_page(context):
    context.app.secondary_listings_page.verify_correct_page_url()


@then('Verify user can go to the final page using the pagination button')
def click_final_page(context):
    context.app.secondary_listings_page.click_next_page()


@then('Verify user can go back to the first page using the pagination button')
def click_prev_page(context):
    context.app.secondary_listings_page.click_prev_page()
    sleep(3)


