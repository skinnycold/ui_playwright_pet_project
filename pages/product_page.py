from time import sleep
import re
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from pages.locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_page_locators = ProductPageLocators(page)

    def choose_size_of_good(self, size: str = "XS"):
        """
        Применяет размер у товара
        :param size: Размер товара - XS, S, M, L, XL
        """
        self.page.locator(f'[option-label="{size}"]').click()

    def choose_color_of_good(self, nth_color: int = 1):
        """
        Применяет цвет у товара
        :param nth_color: Порядковый номер цвета
        """
        self.page.locator('.swatch-option.color').nth(nth_color - 1).click()

    def set_quantity_of_good(self, quantity: int = 1):
        """
        Устанавливает количество товаров
        :param quantity: количество товаров
        """
        self.product_page_locators.quantity_loc.fill(str(quantity))

    def press_add_to_cart_button(self):
        """
        Нажимает на кнопку add to cart
        """
        self.product_page_locators.add_to_cart_button_loc.click()

    def check_size_required_error_message(self, error_text: str = 'This is a required field.'):
        """
        Проверяет отображение сообщения об обязательности установленного размера
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.size_required_error_loc).to_have_text(error_text)

    def check_color_required_error_message(self, error_text: str = 'This is a required field.'):
        """
        Проверяет отображение сообщения об обязательности установленного цвета
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.color_required_error_loc).to_have_text(error_text)

    def press_add_to_wish_list_button(self):
        """
        Нажимает на кнопку Add to wish list
        """
        self.product_page_locators.add_to_wish_list_button_loc.click()

    def press_add_to_compare_button(self):
        """
        Нажимает на кнопку Add to wish list
        """
        self.product_page_locators.add_to_compare_button_loc.click()

    def press_reviews_button(self):
        """
        Нажимает на кнопку review
        """
        self.product_page_locators.reviews_button_loc.click()

    def press_on_rating_star(self, nth_star: int = 1):
        """
        Устанавливает рейтинг товара
        :param nth_star: Выбор звезды рейтинга от 1 до 5
        """
        self.product_page_locators.rating_stars.nth(nth_star).click()

    def fill_nickname_field(self, nickname: str = ''):
        """
        Заполняет поле nickname
        :param nickname: Nickname
        """
        self.product_page_locators.nickname_field_loc.fill(nickname)

    def fill_summary_field(self, summary: str = ''):
        """
        Заполняет поле Summary
        :param summary: Summary
        """
        self.product_page_locators.summary_field_loc.fill(summary)

    def fill_review_field(self, review: str = ''):
        """
        Заполняет поле Review
        :param review: Review
        """
        self.product_page_locators.review_field_loc.fill(review)

    def press_on_submit_review_button(self):
        """
        Нажимает на кнопку submit review
        """
        self.product_page_locators.submit_review_button_loc.click()

    def check_rating_required_error_message(
            self, error_text: str = 'Please select one of each of the ratings above.'
    ):
        """
        Проверяет отображение сообщения об обязательности установленного рейтинга
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.rating_required_error_loc).to_have_text(error_text)

    def check_nickname_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля nickname
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.nickname_required_error_loc).to_have_text(error_text)

    def check_summary_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля summary
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.summary_required_error_loc).to_have_text(error_text)

    def check_review_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля review
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.review_required_error_loc).to_have_text(error_text)

    def check_alert_message(self, alert_text: str = 'You added'):
        """
        Проверяет текст в информационном алерте
        :param alert_text: Текст алерта
        """
        expect(self.product_page_locators.alert_loc).to_have_text(re.compile(alert_text))
