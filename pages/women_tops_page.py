from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.base_product_page import ProductPage
from pages.locators.women_tops_page_locators import WomenTopsPageLocators
import re

class WomenTopsPage(BasePage):
    current_url = '/women/tops-women.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_product_page = ProductPage(page)
        self.locators = WomenTopsPageLocators(page)

    def check_category_jackets_filter(self):
        self.base_product_page.press_category_filter()
        self.locators.category_jackets_filter_log.click()
        expect(self.page).to_have_url(re.compile('cat=23'))
        expect(self.base_product_page.product_page_locators.current_filter_box_loc).to_have_text(re.compile('Jackets'))

    def check_size_xs_filter(self):
        self.base_product_page.press_size_filter()
        self.locators.size_xs_filter_log.click()
        expect(self.page).to_have_url(re.compile('size=166'))
        expect(self.base_product_page.product_page_locators.current_filter_box_loc).to_have_text(re.compile('XS'))

    def check_price_20_29_filter(self):
        self.base_product_page.press_price_filter()
        self.locators.price_20_29_filter_log.click()
        expect(self.page).to_have_url(re.compile('price=20-30'))
        expect(self.base_product_page.product_page_locators.current_filter_box_loc).to_have_text(re.compile(r'\$20\.00 - \$29\.99'))

    """
    !Надо описать все методы для проверок всех фильтров на странице!
    !Подключить аллюр отчеты и добавить в них логирование шагов!
    !Понять как удобно передатб пет проект!
    """