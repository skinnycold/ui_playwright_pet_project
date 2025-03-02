from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.base_product_page import ProductPage

class WomenTopsPage(BasePage):
    current_url = '/women/tops-women.html'

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_product_page = ProductPage(page)


