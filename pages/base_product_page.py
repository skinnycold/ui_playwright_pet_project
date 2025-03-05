from time import sleep

import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.locators.product_page_locators import ProductPageLocators
from pages.enums.enums import SortOption
from pages.enums.enums import LimiterOption
import re


class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.product_page_locators = ProductPageLocators(self.page)

    @allure.step("Получаем список цен")
    def get_prices(self):
        list_prices = [float(price.inner_text().replace('$', '')) for price in self.product_page_locators.list_of_prices_loc.all()]
        allure.attach(f"{list_prices}")
        return list_prices

    @allure.step("Получаем список названий")
    def get_products_names(self):
        list_product_names = [name.inner_text() for name in self.product_page_locators.list_of_products_names_loc.all()]
        allure.attach(f"{list_product_names}")
        return list_product_names

    @allure.step("Получаем количество товаров")
    def get_items(self):
        goods = self.product_page_locators.list_of_items_loc.all()
        allure.attach(f"{len(goods)}")
        return goods

    @allure.step("Применяем сортировку товаров")
    def set_sort_selector(self, select_option: SortOption):
        self.product_page_locators.sort_selector_loc.select_option(select_option.value)

    @allure.step("Устанавливаем количество отображаемых товаров на странице")
    def set_limiter_selector(self, select_option: LimiterOption):
        self.product_page_locators.limiter_selector_loc.select_option(select_option.value)

    @allure.step("Проверяем сортировку товаров")
    def check_sorting(self, select_option: SortOption):
        default_prices_list = self.get_prices()
        default_products_names_list = self.get_products_names()
        if select_option == SortOption.PRICE:
            self.set_sort_selector(select_option)
            self.product_page_locators.list_of_prices_loc.first.wait_for(state='attached')
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
            self.product_page_locators.list_of_prices_loc.first.wait_for(state='attached')
            self.product_page_locators.list_of_products_names_loc.first.wait_for(state='attached')
            position_prices_list = self.get_prices()
            position_products_names_list = self.get_products_names()
            assert default_prices_list == position_prices_list, f"press F"
            assert default_products_names_list == position_products_names_list, f"press F"
        elif select_option == SortOption.PRODUCT_NAME:
            self.set_sort_selector(select_option)
            self.product_page_locators.list_of_products_names_loc.first.wait_for(state='attached')
            sorted_products_names = self.get_products_names()
            expect(self.page).to_have_url(re.compile('product_list_order=name'))
            assert default_products_names_list != sorted_products_names
            assert sorted_products_names == sorted(sorted_products_names),f"""
                Кажется сортировочка поплыла:'(
                
                Начальный список: {default_products_names_list}\n
                
                Отсортированный список: {sorted_products_names}
            """

    @allure.step("Проверяем количество отображаемых товаров")
    def check_item_limiter(self, select_option: LimiterOption):
        if select_option == LimiterOption.SET_12:
            self.set_limiter_selector(select_option)
            self.product_page_locators.list_of_items_loc.first.wait_for(state='attached')
            assert len(self.get_items()) == 12, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """
        elif select_option == LimiterOption.SET_24:
            self.set_limiter_selector(select_option)
            self.product_page_locators.list_of_items_loc.first.wait_for(state='attached')
            expect(self.page).to_have_url(re.compile('product_list_limit=24'))
            assert len(self.get_items()) == 24, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """
        elif select_option == LimiterOption.SET_36:
            self.set_limiter_selector(select_option)
            self.page.wait_for_load_state('networkidle')
            self.product_page_locators.list_of_items_loc.first.wait_for(state='attached')
            expect(self.page).to_have_url(re.compile('product_list_limit=36'))
            assert len(self.get_items()) == 36, f"""
                Фактическое кол-во элементов: {len(self.get_items())}
            """

    def press_category_filter(self):
        self.product_page_locators.category_filter_loc.click()

    def press_style_filter(self):
        self.product_page_locators.style_filter_loc.click()

    def press_size_filter(self):
        self.product_page_locators.size_filter_loc.click()

    def press_climate_filter(self):
        self.product_page_locators.climate_filter_loc.click()

    def press_eco_collection_filter(self):
        self.product_page_locators.eco_collection_filter_loc.click()

    def press_erin_recommends_filter(self):
        self.product_page_locators.erin_recommends_filter_loc.click()

    def press_material_filter(self):
        self.product_page_locators.material_filter_loc.click()

    def press_new_filter(self):
        self.product_page_locators.new_filter_loc.click()

    def press_pattern_filter(self):
        self.product_page_locators.pattern_filter_loc.click()

    def press_performance_fabric_filter(self):
        self.product_page_locators.performance_fabric_filter_loc.click()

    def press_price_filter(self):
        self.product_page_locators.price_filter_loc.click()

    def press_sale_filter(self):
        self.product_page_locators.price_filter_loc.click()