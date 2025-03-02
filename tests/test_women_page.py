from time import sleep

from pages.women_tops_page import WomenTopsPage
from pages.enums.enums import SortOption
from pages.enums.enums import LimiterOption
from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("sort_option",(SortOption.PRICE, SortOption.POSITION, SortOption.PRODUCT_NAME))
def test_sorting(page, sort_option):
    women_tops_page = WomenTopsPage(page)
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_product_page.check_sorting(sort_option)

@pytest.mark.parametrize("limiter_option",(LimiterOption.SET_12, LimiterOption.SET_24, LimiterOption.SET_36))
def test_limiter_items(page, limiter_option):
    women_tops_page = WomenTopsPage(page)
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_product_page.check_item_limiter(limiter_option)

@pytest.mark.parametrize(
    "sort_option, limiter_option", [
        (SortOption.PRICE, LimiterOption.SET_12),
        (SortOption.PRICE, LimiterOption.SET_24),
        (SortOption.PRICE, LimiterOption.SET_36),
        (SortOption.POSITION, LimiterOption.SET_12),
        (SortOption.POSITION, LimiterOption.SET_24),
        (SortOption.POSITION, LimiterOption.SET_36),
        (SortOption.PRODUCT_NAME, LimiterOption.SET_12),
        (SortOption.PRODUCT_NAME, LimiterOption.SET_24),
        (SortOption.PRODUCT_NAME, LimiterOption.SET_36)
    ]
)
def test_sorting_and_limiter(page, sort_option, limiter_option):
    women_tops_page = WomenTopsPage(page)
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_product_page.check_item_limiter(limiter_option)
    women_tops_page.base_product_page.check_sorting(sort_option)
    sleep(3)

def test_category(page):
    women_tops_page = WomenTopsPage(page)
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_product_page.press_category_filter()
    sleep(4)