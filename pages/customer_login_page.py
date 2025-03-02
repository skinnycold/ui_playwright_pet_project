from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import re
from pages.locators.customer_login_page_locators import CustomerLoginPageLocators
from utills.faker_generator import FakerGenerator

class CustomerLoginPage(BasePage):
    current_url = "/customer/account/login/"
    fg = FakerGenerator()

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CustomerLoginPageLocators(page)

    def fill_email_field(self, email: str = 'testtesttest112@mail.com'):
        self.locators.email_field_loc.fill(email)

    def fill_password_field(self, password: str = 'Qwerty1@A'):
        self.locators.password_field_loc.fill(password)

    def press_sign_in_button(self):
        self.locators.sign_in_button_loc.click()

    def check_successful_authorization(self, email: str = "testtesttest112@mail.com"):
        expect(self.locators.personal_information_box_loc).to_have_text(re.compile(email))
        expect(self.locators.title_loc).to_have_text('My Account')

    def check_required_field(self):
        expect(self.locators.email_field_error_loc).to_have_text('This is a required field.')
        expect(self.locators.password_error_loc).to_have_text('This is a required field.')

    def check_unsuccessful_authorization(self):
        expect(self.locators.error_alert_loc).to_have_text(
            "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
        )




