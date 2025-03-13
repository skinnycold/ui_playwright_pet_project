import pytest

@pytest.mark.smoke
def test_successful_full_payment_flow(women_tops_page, base_product_pages, checkout_page):
    """
    Проверяет полный флоу, от добавления товара с продуктовой страницы до успешной оплаты
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    base_product_pages.choose_size_of_good()
    base_product_pages.choose_color_of_good()
    base_product_pages.press_on_the_add_to_card_button()
    base_product_pages.check_information_alert('You added')
    base_product_pages.press_proceed_to_checkout_button()
    checkout_page.fill_email_field()
    checkout_page.fill_first_name_field()
    checkout_page.fill_last_name_field()
    checkout_page.fill_street_address_field()
    checkout_page.fill_city_field()
    checkout_page.set_state_select()
    checkout_page.fill_postal_code_field()
    checkout_page.fill_phone_number_field()
    checkout_page.set_shipping_method()
    checkout_page.press_next_button()
    checkout_page.check_info_box()
    checkout_page.press_place_order()
    checkout_page.check_h1('Thank you for your purchase!')

@pytest.mark.smoke
def test_required_fields(women_tops_page, base_product_pages, checkout_page):
    """
    Проверяет валидацию обязательных полей на странице оплаты
    """
    women_tops_page.open()
    women_tops_page.agree_cookie()
    base_product_pages.choose_size_of_good()
    base_product_pages.choose_color_of_good()
    base_product_pages.press_on_the_add_to_card_button()
    base_product_pages.check_information_alert('You added')
    base_product_pages.press_proceed_to_checkout_button()
    checkout_page.fill_email_field('')
    checkout_page.fill_first_name_field('')
    checkout_page.fill_last_name_field('')
    checkout_page.fill_street_address_field('')
    checkout_page.fill_city_field('')
    checkout_page.set_state_select()
    checkout_page.fill_postal_code_field('')
    checkout_page.fill_phone_number_field('')
    checkout_page.set_shipping_method()
    checkout_page.press_next_button()
    checkout_page.check_email_required_message()
    checkout_page.check_first_name_required_message()
    checkout_page.check_last_name_required_message()
    checkout_page.check_street_address_required_message()
    checkout_page.check_city_required_message()
    checkout_page.check_postal_code_required_message()
    checkout_page.check_phone_number_required_message()


