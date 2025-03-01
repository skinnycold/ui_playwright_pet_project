from playwright.sync_api import Page
from pages.locators.product_page_locators import ProductPageLocators

class ProductPage(ProductPageLocators):

    def __init__(self, page: Page):
        ProductPageLocators.__init__(self, page)
        self.page = page

    def get_prices(self):
        return self.list_of_prices_loc
