import pytest

from pages.product_page import ProductPage
from pages.women_tops_page import WomenTopsPage
from pages.base_products_page import BaseProductsPages

@pytest.fixture()
def product_page(page):
    return ProductPage(page)

@pytest.fixture()
def women_tops_page(page):
    return WomenTopsPage(page)

@pytest.fixture()
def base_product_pages(page):
    return BaseProductsPages(page)