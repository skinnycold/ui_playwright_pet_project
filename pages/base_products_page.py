import allure
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

from pages.locators.base_products_page_locators import BaseProductsPageLocators
from pages.enums.enums import SortOption
from pages.enums.enums import LimiterOption



class BaseProductsPages(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_products_page_locators = BaseProductsPageLocators(self.page)

    @allure.step("Получаем список цен")
    def get_prices(self):
        """
        Вытягивает список цен товаров со страницы
        :return: Список цен
        """
        list_prices = [float(price.inner_text().replace('$', '')) for price in
                       self.base_products_page_locators.list_of_prices_loc.all()]
        allure.attach(f"{list_prices}")
        return list_prices

    @allure.step("Получаем список названий")
    def get_products_names(self):
        """
        Вытягивает список наименований товаров со страницы
        :return: Список наименований товаров
        """
        list_product_names = [name.inner_text() for name in
                              self.base_products_page_locators.list_of_products_names_loc.all()]
        allure.attach(f"{list_product_names}")
        return list_product_names

    @allure.step("Получаем количество товаров")
    def get_items(self):
        """
        Вытягивает все локаторы карточек товаров
        :return: Локаторы карточек товаров
        """
        goods = self.base_products_page_locators.list_of_items_loc.all()
        allure.attach(f"{len(goods)}")
        print(goods)
        return goods

    @allure.step("Применяем сортировку товаров")
    def set_sort_selector(self, select_option: SortOption):
        """
        Применяет сортировку товаров
        :param select_option: Опция сортировки
        """
        self.base_products_page_locators.sort_selector_loc.select_option(select_option.value)

    @allure.step("Устанавливаем количество отображаемых товаров на странице")
    def set_limiter_selector(self, select_option: LimiterOption):
        """
        Применяет лимитер на странице (количество отображаемых товаров)
        :param select_option: Опция лимитера
        """
        self.base_products_page_locators.limiter_selector_loc.select_option(select_option.value)

    @allure.step("Проверяем сортировку товаров")
    def check_sorting(self, select_option: SortOption):
        """
        Проверяет корректность работы примененной сортировки
        :param select_option: Опция сортировки
        """
        default_prices_list = self.get_prices()
        default_products_names_list = self.get_products_names()
        if select_option == SortOption.PRICE:
            self.set_sort_selector(select_option)
            self.base_products_page_locators.list_of_prices_loc.first.wait_for(state='attached')
            price_prices_list = self.get_prices()
            expect(self.page).to_have_url(re.compile('product_list_order=price'))
            assert default_prices_list != price_prices_list, "Кажется сортировочка не применилась"
            assert sorted(price_prices_list) == price_prices_list, f"""
                Кажется сортировочка поплыла:'(
                
                Начальный список: {default_prices_list}\n
                
                Отсортированный список: {price_prices_list}
            """
        elif select_option == SortOption.POSITION:
            self.set_sort_selector(select_option)
            self.base_products_page_locators.list_of_prices_loc.first.wait_for(state='attached')
            self.base_products_page_locators.list_of_products_names_loc.first.wait_for(state='attached')
            position_prices_list = self.get_prices()
            position_products_names_list = self.get_products_names()
            assert default_prices_list == position_prices_list, f"press F"
            assert default_products_names_list == position_products_names_list, f"press F"
        elif select_option == SortOption.PRODUCT_NAME:
            self.set_sort_selector(select_option)
            self.base_products_page_locators.list_of_products_names_loc.first.wait_for(state='attached')
            sorted_products_names = self.get_products_names()
            expect(self.page).to_have_url(re.compile('product_list_order=name'))
            assert default_products_names_list != sorted_products_names
            assert sorted_products_names == sorted(sorted_products_names), f"""
                Кажется сортировочка поплыла:'(
                
                Начальный список: {default_products_names_list}\n
                
                Отсортированный список: {sorted_products_names}
            """

    @allure.step("Проверяем количество отображаемых товаров")
    def check_item_limiter(self, select_option: LimiterOption):
        """
        Проверяет корректность работы примененного лимитера
        :param select_option: Опция лимитера
        """
        if select_option == LimiterOption.SET_12:
            self.set_limiter_selector(select_option)
            self.base_products_page_locators.list_of_items_loc.first.wait_for(state='attached')
            assert len(self.get_items()) == 12, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """
        elif select_option == LimiterOption.SET_24:
            self.set_limiter_selector(select_option)
            self.base_products_page_locators.list_of_items_loc.first.wait_for(state='attached')
            expect(self.page).to_have_url(re.compile('product_list_limit=24'))
            assert len(self.get_items()) == 24, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """
        elif select_option == LimiterOption.SET_36:
            self.set_limiter_selector(select_option)
            self.page.wait_for_load_state('networkidle')
            self.base_products_page_locators.list_of_items_loc.first.wait_for(state='attached')
            expect(self.page).to_have_url(re.compile('product_list_limit=36'))
            assert len(self.get_items()) == 36, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """

    @allure.step("Нажимаем на товар")
    def press_on_the_item(self, nth_item: int = 1):
        """
        Нажимает на товар
        :param nth_item: Номер товара
        :return: Название товара
        """
        item_name = self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).get_attribute('alt')
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).click()
        return item_name

    @allure.step("Применяем размер товара")
    def choose_size_of_good(self, size: str = "XS", nth_item: int = 1):
        """
        Применяет размер у товара
        :param size: Размер товара - XS, S, M, L, XL
        :param nth_item: Номер товара
        """
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).hover()
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).locator(f'[option-label="{size}"]').click()

    @allure.step("Проверяем цвет товара")
    def choose_color_of_good(self, color: str = "White", nth_item: int = 1):
        """
        Применяет цвет у товара
        :param color: Purple, White и тд.
        :param nth_item: Номер товара
        """
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).hover()
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).locator(
            f'[option-label="{color}"]').click()

    @allure.step("Добавляем товар в корзину")
    def press_on_the_add_to_card_button(self, nth_item: int = 1):
        """
        Нажимает на кнопку add to card выбранного товара
        :param nth_item: Номер товара
        """
        self.base_products_page_locators.list_of_items_loc.nth(nth_item - 1).hover()
        self.base_products_page_locators.add_to_card_buttons.nth(nth_item - 1).click()

    @allure.step("Проверяем изменение режима отображения товара")
    def press_and_check_list_view(self):
        """
        Применяет отображение товаров в лист моде, и проверяет, что фильтр применился
        """
        self.base_products_page_locators.list_mode_button_loc.click()
        expect(self.page).to_have_url(re.compile('product_list_mode=list'))

    @allure.step("Проверяем количество добавленных товаров в корзину")
    def check_counter_number(self, expected_number_of_goods: int = 1):
        """
        Проверяет количество добавленных товаров в корзину
        :param expected_number_of_goods: Ожидаемое количество товаров добавленных в корзину
        """
        expect(self.base_products_page_locators.counter_number_in_shopping_card).to_have_text(
            f"{expected_number_of_goods}")

    def press_category_filter(self):
        self.base_products_page_locators.category_filter_loc.click()

    def press_style_filter(self):
        self.base_products_page_locators.style_filter_loc.click()

    def press_size_filter(self):
        self.base_products_page_locators.size_filter_loc.click()

    def press_climate_filter(self):
        self.base_products_page_locators.climate_filter_loc.click()

    def press_eco_collection_filter(self):
        self.base_products_page_locators.eco_collection_filter_loc.click()

    def press_erin_recommends_filter(self):
        self.base_products_page_locators.erin_recommends_filter_loc.click()

    def press_material_filter(self):
        self.base_products_page_locators.material_filter_loc.click()

    def press_new_filter(self):
        self.base_products_page_locators.new_filter_loc.click()

    def press_pattern_filter(self):
        self.base_products_page_locators.pattern_filter_loc.click()

    def press_performance_fabric_filter(self):
        self.base_products_page_locators.performance_fabric_filter_loc.click()

    def press_price_filter(self):
        self.base_products_page_locators.price_filter_loc.click()

    def press_sale_filter(self):
        self.base_products_page_locators.price_filter_loc.click()

    @allure.step("Проверяем текст в информационном алерте")
    def check_information_alert(self, information_text):
        """
        Проверяет текст информационного алерта на странице
        :param information_text: Ожидаемый текст алерта
        """
        self.base_products_page_locators.information_alert_loc.wait_for(state='attached')
        self.base_products_page_locators.information_alert_loc.wait_for(state='visible')
        expect(self.base_products_page_locators.information_alert_loc).to_have_text(re.compile(information_text))

    @allure.step("Нажимаем на кнопку proceed to checkout")
    def press_proceed_to_checkout_button(self):
        """
        Нажимает на кнопку proceed to checkout (для перехода к этапу оплаты товара)
        """
        self.base_products_page_locators.cart_loc.hover()
        self.base_products_page_locators.cart_loc.click()
        self.page.mouse.down()
        self.base_products_page_locators.cart_proceed_to_checkout_loc.hover()
        self.base_products_page_locators.cart_proceed_to_checkout_loc.wait_for(state='visible')
        self.page.mouse.up()
        self.base_products_page_locators.cart_proceed_to_checkout_loc.click()
        self.page.wait_for_load_state(state='load')
