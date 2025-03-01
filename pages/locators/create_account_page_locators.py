from playwright.sync_api import Page

class CreateAccountPageLocators:
    def __init__(self, page: Page):
        self.first_name_field_loc = page.locator('#firstname')
        self.last_name_field_loc = page.locator('#lastname')
        self.email_field_loc = page.locator('#email_address')
        self.password_field_loc = page.locator('#password')
        self.confirm_password_field_loc = page.locator('#password-confirmation')
        self.create_an_account_button = page.get_by_role('button', name='Create an Account')
        self.first_name_error_loc = page.locator('#firstname-error')
        self.last_name_error_loc = page.locator('#lastname-error')
        self.email_error_loc = page.locator('#email_address-error')
        self.password_error_loc = page.locator('#password-error')
        self.confirm_password_error_loc = page.locator('#password-confirmation-error')
        self.success_registration_alert_loc = page.get_by_role('alert').locator('nth=0')
        self.personal_information_box_loc = page.locator('.box.box-information')
        self.page_messages_error_loc = page.locator('.page.messages')
        self.cookie_agree_button_loc = page.locator('.css-1n36tvh')

