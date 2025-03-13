from playwright.sync_api import Page
class CheckoutPageLocators:
    def __init__(self, page: Page):
        self.email_field_loc = page.locator('[name="username"][id="customer-email"]').first
        self.email_field_error_message_loc = page.locator('[id="customer-email-error"]')

        self.first_name_field_loc = page.locator('[name="firstname"]')
        self.first_name_field_error_message_loc = page.locator(
            '[name="shippingAddress.firstname"] [class="control"] [class="field-error"] span'
        )

        self.last_name_field_loc = page.locator('[name="lastname"]')
        self.last_name_field_error_message_loc = page.locator(
            '[name="shippingAddress.lastname"] [class="control"] [class="field-error"] span'
        )

        self.street_address_field_loc = page.locator('[name="street[0]"]')
        self.street_address_field_error_message_loc = page.locator(
            '[name="shippingAddress.street.0"] [class="control"] [class="field-error"] span'
        )

        self.city_field_loc = page.locator('[name="city"]')
        self.city_field_error_message_loc = page.locator(
            '[name="shippingAddress.city"] [class="control"] [class="field-error"] span'
        )

        self.state_select_loc = page.locator('[name="region_id"]')
        self.postal_code_loc = page.locator('[name="postcode"]')
        self.postal_code_error_message_loc = page.locator(
            '[name="shippingAddress.postcode"] [class="control"] [class="field-error"] span'
        )

        self.phone_number_loc = page.locator('[name="telephone"]')
        self.phone_number_error_message_loc = page.locator(
            '[name="shippingAddress.telephone"] [class="control _with-tooltip"] [class="field-error"] span'
        )

        self.shipping_methods_loc = page.locator('tbody tr td input')

        self.next_button_loc = page.locator('.button.action.continue.primary')

        self.place_order_button_loc = page.locator('[class="action primary checkout"]')

        self.check_information_box_loc = page.locator('.billing-address-details')
