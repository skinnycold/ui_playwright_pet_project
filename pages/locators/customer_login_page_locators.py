from playwright.sync_api import Page

class CustomerLoginPageLocators:
    def __init__(self, page: Page):
        self.email_field_loc = page.locator('#email')
        self.password_field_loc = page.locator('#pass').locator('nth=0')
        self.sign_in_button_loc = page.get_by_role('button', name='Sign In')
        self.email_field_error_loc = page.locator('#email-error')
        self.password_error_loc = page.locator('#pass-error')
        self.personal_information_box_loc = page.locator('.box.box-information')
        self.title_loc = page.locator('h1')
        self.new_customer_info_loc = page.locator('#block-new-customer-heading').locator('nth=0')
        self.error_alert_loc = page.locator("[role='alert']").locator('nth=0')