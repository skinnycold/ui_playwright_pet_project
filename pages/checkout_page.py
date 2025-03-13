import allure
import re
from playwright.sync_api import Page, expect
from utills.faker_generator import FakerGenerator

from pages.base_page import BasePage
from pages.locators.checkout_page_locators import CheckoutPageLocators




class CheckoutPage(BasePage):
    fg = FakerGenerator()
    _error_message = 'This is a required field.'

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_page_locators = CheckoutPageLocators(page)
        self._email = None
        self._first_name = None
        self._last_name = None
        self._street_address = None
        self._city = None
        self._postal_code = None
        self._phone_number = None

    @allure.step("Заполняем поле Email Address")
    def fill_email_field(self, email: str = fg.generate_email()):
        """
        Заполняет поле Email Address
        :param email: email
        """
        self._email = email
        self.checkout_page_locators.email_field_loc.wait_for(state="visible")
        self.checkout_page_locators.email_field_loc.fill(email)

    @allure.step("Заполняем поле First Name")
    def fill_first_name_field(self, first_name: str = fg.generate_first_name()):
        """
        Заполняет поле First Name
        :param first_name: Имя
        """
        self._first_name = first_name
        self.checkout_page_locators.first_name_field_loc.fill(first_name)

    @allure.step("Заполняем поле Last Name")
    def fill_last_name_field(self, last_name: str = fg.generate_last_name()):
        """
        Заполняет поле Last Name
        :param last_name: Фамилия
        """
        self._last_name = last_name
        self.checkout_page_locators.last_name_field_loc.fill(last_name)

    @allure.step("Заполняем поле Street Address")
    def fill_street_address_field(self, street_address: str = fg.generate_street_name()):
        """
        Заполняет поле Street Address
        :param street_address: Улица
        """
        self._street_address = street_address
        self.checkout_page_locators.street_address_field_loc.fill(street_address)

    @allure.step("Заполняем поле City")
    def fill_city_field(self, city: str = fg.generate_city()):
        """
        Заполняет поле City
        :param city: Город
        """
        self._city = city
        self.checkout_page_locators.city_field_loc.fill(city)

    @allure.step("Выбираем штат")
    def set_state_select(self, country: str = 'Alaska'):
        """
        Выбирает штат в селекторе
        :param country: Штат
        """
        self.checkout_page_locators.state_select_loc.select_option(country)

    @allure.step("Заполняем поле Postal Code")
    def fill_postal_code_field(self, postal_code: str = fg.generate_postal_code()):
        """
        Заполняет поле Postal Code
        :param postal_code: Почтовый индекс
        """
        self._postal_code = postal_code
        self.checkout_page_locators.postal_code_loc.fill(postal_code)

    @allure.step("Заполняем поле Phone Number")
    def fill_phone_number_field(self, phone_number: str = fg.generate_phone_number()):
        """
        Заполняет поле Phone Number
        :param phone_number: Номер телефона
        """
        self._phone_number = phone_number
        self.checkout_page_locators.phone_number_loc.fill(phone_number)

    def set_shipping_method(self, nth_method: int = 1):
        # expect(element).to_be_enabled(timeout=5000)
        self.checkout_page_locators.shipping_methods_loc.nth(nth_method - 1).click()

    @allure.step("Заполняем поле Phone Number")
    def press_next_button(self):
        """
        Нажимает на кнопку Next
        """
        self.checkout_page_locators.next_button_loc.click()

    @allure.step("Проверяем обязательность поля Email")
    def check_email_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.email_field_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля First name")
    def check_first_name_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.first_name_field_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля Last name")
    def check_last_name_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.last_name_field_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля Street address")
    def check_street_address_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.street_address_field_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля City")
    def check_city_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.city_field_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля Postal code")
    def check_postal_code_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.postal_code_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем обязательность поля Phone number")
    def check_phone_number_required_message(self, error_message: str = _error_message):
        """
        Проверяет появление ошибки об обязательности заполнения поля
        :param error_message: Текст ошибки
        """
        expect(self.checkout_page_locators.phone_number_error_message_loc).to_have_text(error_message)

    @allure.step("Проверяем пользовательскую информацию")
    def check_info_box(self, name: str = None, lastname: str = None, city: str = None, postalcode: str = None):
        """
        Проверяет пользовательскую информацию перед покупкой
        :param name: Имя
        :param lastname: Фамилия
        :param city: Город
        :param postalcode: Почтовый индекс
        """
        name = name or self._first_name
        lastname = lastname or self._last_name
        city = city or self._city
        postalcode = postalcode or self._postal_code
        pattern = re.compile(
            f"(?=.*{re.escape(name)})(?=.*{re.escape(lastname)})(?=.*{re.escape(city)})(?=.*{re.escape(postalcode)})",
            re.DOTALL
        )
        expect(self.checkout_page_locators.check_information_box_loc).to_have_text(pattern)

    @allure.step("Нажимаем на кнопку Place Order")
    def press_place_order(self):
        """
        Нажимает на кнопку Place Order
        """
        self.checkout_page_locators.place_order_button_loc.click()
