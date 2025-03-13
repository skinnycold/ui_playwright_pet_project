from playwright.sync_api import Page

class ProductPageLocators:

    def __init__(self, page: Page):
        self.quantity_loc = page.locator('#qty')
        self.add_to_cart_button_loc = page.get_by_role('button', name='Add to Cart')
        self.size_required_error_loc = page.locator("[id='super_attribute[143]-error']")
        self.color_required_error_loc = page.locator("[id='super_attribute[93]-error']")
        self.add_to_wish_list_button_loc = page.get_by_role('link', name='Add to Wish List')
        self.add_to_compare_button_loc = page.get_by_role('link', name='Add to Compare')
        self.reviews_button_loc = page.locator('[id="tab-label-reviews-title"]')
        self.nickname_field_loc = page.locator('#nickname_field')
        self.summary_field_loc = page.locator('#summary_field')
        self.review_field_loc = page.locator('#review_field')
        self.submit_review_button_loc = page.locator('.action.submit.primary')
        self.rating_required_error_loc = page.locator("[id='ratings[4]-error']")
        self.nickname_required_error_loc = page.locator('#nickname_field-error')
        self.summary_required_error_loc = page.locator("[id='summary_field-error']")
        self.review_required_error_loc = page.locator('[id="review_field-error"]')
        self.alert_loc = page.locator('[role="alert"]').first