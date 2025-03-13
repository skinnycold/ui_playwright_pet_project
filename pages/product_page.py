import allure
import re
from playwright.sync_api import Page, expect
from utills.faker_generator import FakerGenerator

from pages.base_page import BasePage
from pages.locators.product_page_locators import ProductPageLocators



class ProductPage(BasePage):
    fg = FakerGenerator()

    def __init__(self, page: Page):
        super().__init__(page)
        self.product_page_locators = ProductPageLocators(page)

    @allure.step("Выбираем размер товара")
    def choose_size_of_good(self, size: str = "XS"):
        """
        Применяет размер у товара
        :param size: Размер товара - XS, S, M, L, XL
        """
        self.page.locator(f'[option-label="{size}"]').click()

    @allure.step("Выбираем цвет товара")
    def choose_color_of_good(self, nth_color: int = 1):
        """
        Применяет цвет у товара
        :param nth_color: Порядковый номер цвета
        """
        self.page.locator('.swatch-option.color').nth(nth_color - 1).click()

    @allure.step("Устанавливаем количество товара")
    def set_quantity_of_good(self, quantity: int = 1):
        """
        Устанавливает количество товаров
        :param quantity: количество товаров
        """
        self.product_page_locators.quantity_loc.fill(str(quantity))

    @allure.step("Нажимаем на кнопку add to cart")
    def press_add_to_cart_button(self):
        """
        Нажимает на кнопку add to cart
        """
        self.product_page_locators.add_to_cart_button_loc.click()

    @allure.step("Валидируем обязательность выбора размера")
    def check_size_required_error_message(self, error_text: str = 'This is a required field.'):
        """
        Проверяет отображение сообщения об обязательности установленного размера
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.size_required_error_loc).to_have_text(error_text)

    @allure.step("Валидируем обязательность выбора цвета")
    def check_color_required_error_message(self, error_text: str = 'This is a required field.'):
        """
        Проверяет отображение сообщения об обязательности установленного цвета
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.color_required_error_loc).to_have_text(error_text)

    @allure.step("Нажимаем на кнопку add to wish list")
    def press_add_to_wish_list_button(self):
        """
        Нажимает на кнопку Add to wish list
        """
        self.product_page_locators.add_to_wish_list_button_loc.click()

    @allure.step("Нажимаем на кнопку add to compare")
    def press_add_to_compare_button(self):
        """
        Нажимает на кнопку Add to compare
        """
        self.product_page_locators.add_to_compare_button_loc.click()

    @allure.step("Нажимаем на кнопку review")
    def press_reviews_button(self):
        """
        Нажимает на кнопку review
        """
        self.product_page_locators.reviews_button_loc.click()

    @allure.step("Выбираем рейтинг товара")
    def press_on_rating_star(self, nth_star: int = 1):
        """
        Устанавливает рейтинг товара
        :param nth_star: Выбор звезды рейтинга от 1 до 5
        """
        if 1 <= nth_star <= 5:
            self.page.locator(f'#Rating_{nth_star}_label').wait_for(state='attached')
            self.page.evaluate(f"document.querySelector('#Rating_{nth_star}_label').click()")
        else:
            raise ValueError('Введи от 1 до 5')

    @allure.step("Заполняем поле nickname")
    def fill_nickname_field(self, nickname: str = fg.generate_first_name()):
        """
        Заполняет поле nickname
        :param nickname: Nickname
        """
        self.product_page_locators.nickname_field_loc.fill(nickname)

    @allure.step("Заполняем поле summary")
    def fill_summary_field(self, summary: str = fg.generate_text(20)):
        """
        Заполняет поле Summary
        :param summary: Summary
        """
        self.product_page_locators.summary_field_loc.fill(summary)

    @allure.step("Заполняем поле review")
    def fill_review_field(self, review: str = fg.generate_text(100)):
        """
        Заполняет поле Review
        :param review: Review
        """
        self.product_page_locators.review_field_loc.fill(review)

    @allure.step("Нажимаем на кнопку submit review")
    def press_on_submit_review_button(self):
        """
        Нажимает на кнопку submit review
        """
        self.product_page_locators.submit_review_button_loc.click()

    @allure.step("Валидируем обязательность выбора рейтинга")
    def check_rating_required_error_message(
            self, error_text: str = 'Please select one of each of the ratings above.'
    ):
        """
        Проверяет отображение сообщения об обязательности установленного рейтинга
        :param error_text: Текст ошибки
        """
        self.product_page_locators.rating_required_error_loc.wait_for(state='visible')
        expect(self.product_page_locators.rating_required_error_loc).to_have_text(error_text)

    @allure.step("Валидируем обязательность заполнения поля nickname")
    def check_nickname_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля nickname
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.nickname_required_error_loc).to_have_text(error_text)

    @allure.step("Валидируем обязательность заполнения поля summary")
    def check_summary_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля summary
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.summary_required_error_loc).to_have_text(error_text)

    @allure.step("Валидируем обязательность заполнения поля review")
    def check_review_required_error_message(
            self, error_text: str = 'This is a required field.'
    ):
        """
        Проверяет отображение сообщения об обязательности заполненного поля review
        :param error_text: Текст ошибки
        """
        expect(self.product_page_locators.review_required_error_loc).to_have_text(error_text)

    @allure.step("Проверяем сообщение в информационном Алерте")
    def check_alert_message(self, alert_text: str = 'You added'):
        """
        Проверяет текст в информационном алерте
        :param alert_text: Текст алерта
        """

        print("Waiting for alert to be attached...")
        self.product_page_locators.alert_loc.wait_for(state='attached', timeout=5000)
        print("Waiting for alert to be visible...")
        self.product_page_locators.alert_loc.wait_for(state='visible', timeout=30000)
        expect(self.product_page_locators.alert_loc).to_have_text(re.compile(alert_text), timeout=30000)
