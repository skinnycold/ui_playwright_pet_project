import pytest


@pytest.mark.smoke
def test_positive_adding_product_to_cart(women_tops_page, product_page):
    """
    Проверяет успешное добавление товара в корзину
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_size_of_good("L")
    product_page.choose_color_of_good()
    product_page.set_quantity_of_good(2)
    product_page.press_add_to_cart_button()
    women_tops_page.base_products_pages.check_counter_number(2)
    product_page.check_alert_message('You added')


@pytest.mark.smoke
def test_adding_product_without_size_and_color(women_tops_page, product_page):
    """
    Проверяет добавление товара в корзину без установленных параметрах размера и цвета
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.set_quantity_of_good()
    product_page.press_add_to_cart_button()
    product_page.check_size_required_error_message('This is a required field.')
    product_page.check_color_required_error_message('This is a required field.')


@pytest.mark.regression
def test_adding_product_without_size(women_tops_page, product_page):
    """
    Проверяет добавление товара в корзину без установленного размера
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_color_of_good(3)
    product_page.set_quantity_of_good(3)
    product_page.press_add_to_cart_button()
    product_page.check_size_required_error_message('This is a required field.')


@pytest.mark.regression
def test_adding_product_without_color(women_tops_page, product_page):
    """
    Проверяет добавление товара в корзину без установленного цвета
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_size_of_good("S")
    product_page.set_quantity_of_good(2)
    product_page.press_add_to_cart_button()
    product_page.check_color_required_error_message('This is a required field.')


@pytest.mark.smoke
def test_adding_product_to_compare(women_tops_page, product_page):
    """
    Проверяет добавление товара в раздел сравнения товаров
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_size_of_good("S")
    product_page.press_add_to_compare_button()
    product_page.check_alert_message('You added')


@pytest.mark.smoke
def test_sending_review(women_tops_page, product_page):
    """
    Проверяет успешную отправку ревью отзыва
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.press_reviews_button()
    product_page.press_on_rating_star(5)
    product_page.fill_nickname_field()
    product_page.fill_summary_field()
    product_page.fill_review_field()
    product_page.press_on_submit_review_button()
    product_page.check_alert_message('You submitted your review for moderation.')


@pytest.mark.smoke
def test_sending_review_without_required_fields(women_tops_page, product_page):
    """
    Проверяет обязательные поля в разделе ревью
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.press_reviews_button()
    product_page.fill_nickname_field('')
    product_page.fill_summary_field('')
    product_page.fill_review_field('')
    product_page.press_on_submit_review_button()
    product_page.check_rating_required_error_message()
    product_page.check_nickname_required_error_message()
    product_page.check_summary_required_error_message()
    product_page.check_review_required_error_message()
