import allure
import re
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.base_products_page import BaseProductsPages
from pages.locators.women_tops_page_locators import WomenTopsPageLocators


class WomenTopsPage(BasePage):
    current_url = '/women/tops-women.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_products_pages = BaseProductsPages(page)
        self.locators = WomenTopsPageLocators(page)


    def press_filter(self, category_filter_locator, subcategory_filter_locator):
        with allure.step("Применяем фильтр:"):
            allure.attach(
                f"{getattr(self.base_products_pages.base_products_page_locators, category_filter_locator).inner_text()}"
            )
            getattr(self.base_products_pages.base_products_page_locators, category_filter_locator).click()
            allure.attach(
                f"{getattr(self.locators, subcategory_filter_locator).inner_text()}"
            )
            getattr(self.locators, subcategory_filter_locator).click()

    @allure.step("Проверяем примененный фильтр")
    def check_filter(self, url_parameter, filter_name):
        expect(self.page).to_have_url(re.compile(url_parameter))
        expect(self.base_products_pages.base_products_page_locators.current_filter_box_loc).to_have_text(re.compile(filter_name))

