import pytest
from pages.product_page import ProductPage
from pages.women_tops_page import WomenTopsPage
from pages.base_products_page import BaseProductsPages


@pytest.mark.smoke
def test_positive_adding_product_to_cart(women_tops_page, product_page):
    """
    Проверяет успешное добавление товара в корзину

    Шаги:
    1. Открываем страницу с женскими топами
    2. Переходим на страницу товара
    3. Выбираем размер
    4. Выбираем цвет
    5. Указываем количество товаров
    6. Добавляем товар в корзину
    7. Проверяем количество добавленных товаров в корзине
    8. Проверяем появление уведомления об успешном добавлении
    """
    women_tops_page.open()
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

    Шаги:
    1. Открываем страницу с женскими топами
    2. Переходим на страницу товара
    3. Указываем количество товаров
    4. Добавляем товар в корзину
    5. Проверяем сообщение о том что поле размера обязательно
    6. Проверяем сообщение о том что поле цвета обязательно
    """
    women_tops_page.open()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.set_quantity_of_good()
    product_page.press_add_to_cart_button()
    product_page.check_size_required_error_message('This is a required field.')
    product_page.check_color_required_error_message('This is a required field.')

@pytest.mark.regression
def test_adding_product_without_size(women_tops_page, product_page):
    """
    Проверяет добавление товара в корзину без установленного размера

    Шаги:
    1. Открываем страницу с женскими топами
    2. Переходим на страницу товара
    3. Выбираем цвет
    4. Указываем количество товаров
    5. Добавляем товар в корзину
    6. Проверяем сообщение о том что поле размера обязательно
    """
    women_tops_page.open()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_color_of_good(3)
    product_page.set_quantity_of_good(3)
    product_page.press_add_to_cart_button()
    product_page.check_size_required_error_message('This is a required field.')


@pytest.mark.regression
def test_adding_product_without_color(women_tops_page, product_page):
    """
    Проверяет добавление товара в корзину без установленного цвета

    Шаги:
    1. Открываем страницу с женскими топами
    2. Переходим на страницу товара
    3. Выбираем размер
    4. Указываем количество товаров
    5. Добавляем товар в корзину
    6. Проверяем сообщение о том что поле цвета обязательно
    """
    women_tops_page.open()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_size_of_good("S")
    product_page.set_quantity_of_good(2)
    product_page.press_add_to_cart_button()
    product_page.check_color_required_error_message('This is a required field.')

@pytest.mark.smoke
def test_adding_product_to_compare(women_tops_page, product_page):
    """
    Проверяет добавление товара в раздел сравнения товаров

    Шаги:
    1. Открываем страницу с женскими топами
    2. Переходим на страницу товара
    3. Выбираем размер
    4. Нажимаем на кнопку Add to compare
    5. Проверяем появление уведомления об успешном добавлении товара в раздел сравнения
    """
    women_tops_page.open()
    women_tops_page.base_products_pages.press_on_the_item()
    product_page.choose_size_of_good("S")
    product_page.press_add_to_compare_button()
    product_page.check_alert_message('You added')