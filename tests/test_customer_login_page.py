from time import sleep
import pytest

from pages.customer_login_page import CustomerLoginPage

def test_successful_authorization(page):
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.open()
    customer_login_page.fill_email_field()
    customer_login_page.fill_password_field()
    customer_login_page.press_sign_in_button()
    customer_login_page.check_successful_authorization()

def test_required_fields(page):
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.open()
    customer_login_page.wait_full_load_page()
    customer_login_page.fill_email_field(' ')
    customer_login_page.fill_password_field('')
    customer_login_page.press_sign_in_button()
    customer_login_page.check_required_field()

@pytest.mark.parametrize(
    'email, password', [('testtesttest112@mail.com', 'qrfqw@1A'), ('qrfqw@mail.com', 'werty1@A')]
)
def test_unsuccessful_authorization(page, email, password):
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.open()
    customer_login_page.fill_email_field(email)
    customer_login_page.fill_password_field(password)
    customer_login_page.press_sign_in_button()
    customer_login_page.check_unsuccessful_authorization()