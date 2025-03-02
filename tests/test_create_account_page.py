from pages.create_account_page import CreateAccountPage

from time import sleep

def test_successful_registration(page):
    create_account_page = CreateAccountPage(page)
    create_account_page.open()
    create_account_page.wait_full_load_page()
    create_account_page.agree_cookie()
    create_account_page.fill_first_name_field()
    create_account_page.fill_last_name_field()
    create_account_page.fill_email_field()
    create_account_page.fill_password_field()
    create_account_page.fill_confirm_password_field()
    create_account_page.press_create_an_account_button()
    create_account_page.check_successful_registration()

def test_required_fields(page):
    create_account_page = CreateAccountPage(page)
    create_account_page.open()
    create_account_page.agree_cookie()
    create_account_page.fill_first_name_field('')
    create_account_page.fill_last_name_field('')
    create_account_page.fill_email_field('')
    create_account_page.fill_password_field('')
    create_account_page.fill_confirm_password_field('')
    create_account_page.press_create_an_account_button()
    create_account_page.check_required_field()

def test_same_mail_registration(page):
    create_account_page = CreateAccountPage(page)
    create_account_page.open()
    create_account_page.agree_cookie()
    create_account_page.fill_first_name_field()
    create_account_page.fill_last_name_field()
    create_account_page.fill_email_field('testtesttest@mail.com')
    create_account_page.fill_password_field()
    create_account_page.fill_confirm_password_field()
    create_account_page.press_create_an_account_button()
    create_account_page.check_same_mail_registration()