import pytest


@pytest.mark.smoke
def test_successful_authorization(customer_login_page):
    """
    Проверяет успешную аутентификацию
    """
    customer_login_page.open()
    customer_login_page.wait_full_load_page()
    customer_login_page.agree_cookie()
    customer_login_page.fill_email_field()
    customer_login_page.fill_password_field()
    customer_login_page.press_sign_in_button()
    customer_login_page.check_successful_authorization()


@pytest.mark.smoke
def test_required_fields(customer_login_page):
    """
    Проверяет валидацию обязательных полей на странице аутентификации
    """
    customer_login_page.open()
    customer_login_page.wait_full_load_page()
    customer_login_page.agree_cookie()
    customer_login_page.wait_full_load_page()
    customer_login_page.fill_email_field(' ')
    customer_login_page.fill_password_field('')
    customer_login_page.press_sign_in_button()
    customer_login_page.check_required_field()


@pytest.mark.smoke
@pytest.mark.parametrize(
    'email, password', [('testtesttest112@mail.com', 'qrfqw@1A'), ('qrfqw@mail.com', 'werty1@A')]
)
def test_unsuccessful_authorization(customer_login_page, email, password):
    """
    Проверяет попытки аутентификации с корректным email и неверным паролем, и наоборот
    """
    customer_login_page.open()
    customer_login_page.wait_full_load_page()
    customer_login_page.agree_cookie()
    customer_login_page.fill_email_field(email)
    customer_login_page.fill_password_field(password)
    customer_login_page.press_sign_in_button()
    customer_login_page.check_unsuccessful_authorization()
