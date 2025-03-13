from pages.enums.enums import SortOption
from pages.enums.enums import LimiterOption
from data.women_tops_page_data import data_filters
import pytest



@pytest.mark.parametrize("sort_option", (SortOption.PRICE, SortOption.POSITION, SortOption.PRODUCT_NAME))
def test_sorting(women_tops_page, sort_option):
    """
    Проверяет функциональность сортировки
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.check_sorting(sort_option)



@pytest.mark.parametrize("limiter_option", (LimiterOption.SET_12, LimiterOption.SET_24, LimiterOption.SET_36))
def test_limiter_items(women_tops_page, limiter_option):
    """
    Проверяет функциональность изменения видимого количества товаров на странице
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.check_item_limiter(limiter_option)



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
def test_sorting_and_limiter(women_tops_page, sort_option, limiter_option):
    """
    Проверяет функциональность сортировки и изменения видимого количества товаров на странице
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.check_item_limiter(limiter_option)
    women_tops_page.base_products_pages.check_sorting(sort_option)



@pytest.mark.parametrize(
    "category_filter_locator, subcategory_filter_locator, filter_name, url_parameter",
    data_filters
)
def test_filters(
        women_tops_page, category_filter_locator, subcategory_filter_locator, filter_name, url_parameter
):
    """
    Проверяет функциональность фильтрации товаров
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.press_filter(category_filter_locator, subcategory_filter_locator)
    women_tops_page.check_filter(url_parameter, filter_name)



def test_list_view(women_tops_page):
    """
    Проверяет функциональность изменения вида отображаемых товаров (Grid, List)
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_and_check_list_view()


@pytest.mark.smoke
def test_full_flow_adding_goods(women_tops_page):
    """
    Проверяет успешное добавление товара в корзину с продуктовой страницы
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.choose_size_of_good(nth_item=3)
    women_tops_page.base_products_pages.choose_color_of_good(nth_item=3)
    women_tops_page.base_products_pages.press_on_the_add_to_card_button(nth_item=3)
    women_tops_page.base_products_pages.choose_size_of_good(nth_item=1)
    women_tops_page.base_products_pages.choose_color_of_good(nth_item=1)
    women_tops_page.base_products_pages.press_on_the_add_to_card_button(nth_item=1)
    women_tops_page.base_products_pages.check_counter_number(2)
