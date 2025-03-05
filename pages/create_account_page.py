import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.locators.create_account_page_locators import CreateAccountPageLocators
import re
from utills.faker_generator import FakerGenerator
import allure


class CreateAccountPage(BasePage):
    fg = FakerGenerator()
    current_url = '/customer/account/create/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CreateAccountPageLocators(page)

    @allure.step("Заполняем поле: Имя")
    def fill_first_name_field(self, first_name: str = fg.first_name):
        self.locators.first_name_field_loc.fill(first_name)

    @allure.step("Заполняем поле: Фамилия")
    def fill_last_name_field(self, last_name: str = fg.last_name):
        self.locators.last_name_field_loc.fill(last_name)

    @allure.step("Заполняем поле: Email")
    def fill_email_field(self, email=fg.email):
        self.locators.email_field_loc.fill(email)

    @allure.step("Заполняем поле: Пароль")
    def fill_password_field(self, password: str = fg.password):
        self.locators.password_field_loc.fill(password)

    @allure.step("Заполняем поле: Подтверждение пароля")
    def fill_confirm_password_field(self, confirm_password: str = fg.password):
        self.locators.confirm_password_field_loc.fill(confirm_password)

    @allure.step("Нажимаем на кнопку: Create account")
    def press_create_an_account_button(self):
        self.locators.create_an_account_button.click()

    @allure.step("Валидируем обязательные поля")
    def check_required_field(self):
        expect(self.locators.first_name_error_loc).to_have_text('This is a required field.')
        expect(self.locators.last_name_error_loc).to_have_text('This is a required field.')
        expect(self.locators.email_error_loc).to_have_text('This is a required field.')
        expect(self.locators.password_error_loc).to_have_text('This is a required field.')
        expect(self.locators.confirm_password_error_loc).to_have_text('This is a required field.')

    @allure.step("Проверяем успешную регистрацию")
    def check_successful_registration(self, email: str = fg.email):
        expect(self.locators.success_registration_alert_loc).to_have_text(
            'Thank you for registering with Main Website Store.')
        expect(self.locators.personal_information_box_loc).to_have_text(re.compile(email))

    @allure.step("Проверяем регистрацию с существующим email")
    def check_same_mail_registration(self):
        expect(self.locators.page_messages_error_loc).to_have_text(
            re.compile('There is already an account with this email address.')
        )
