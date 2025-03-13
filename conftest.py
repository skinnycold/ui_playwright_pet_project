import pytest

from pages.product_page import ProductPage
from pages.women_tops_page import WomenTopsPage
from pages.base_products_page import BaseProductsPages
from pages.checkout_page import CheckoutPage
from pages.create_account_page import CreateAccountPage
from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage


@pytest.fixture()
def product_page(page):
    return ProductPage(page)

@pytest.fixture()
def women_tops_page(page):
    return WomenTopsPage(page)

@pytest.fixture()
def base_product_pages(page):
    return BaseProductsPages(page)

@pytest.fixture()
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(page)

@pytest.fixture()
def customer_login_page(page):
    return CustomerLoginPage(page)

@pytest.fixture()
def home_page(page):
    return HomePage(page)