from playwright.sync_api import Page

class BaseProductsPageLocators:
    def __init__(self, page: Page):
        self.list_of_prices_loc = page.locator('//*[@data-price-type="finalPrice"]/span')
        self.list_of_products_names_loc = page.locator('.product.name.product-item-name')
        self.list_of_items_loc = page.locator('.item.product.product-item') # было .item.product.product-item
        self.add_to_card_buttons = page.locator('.action.tocart.primary')
        self.size_of_good_buttons = page.locator('[option-label="XS"]')
        self.grid_mode_button_loc = page.locator('mode-grid').first
        self.list_mode_button_loc = page.locator('#mode-list').first
        self.sort_selector_loc = page.locator('#sorter').locator('nth=0')
        self.limiter_selector_loc = page.locator('#limiter').locator('nth=1')
        self.current_filter_box_loc = page.locator('.filter-current')
        self.counter_number_in_shopping_card = page.locator('.counter-number')

        self.category_filter_loc = page.get_by_role('tab', name='Category')
        self.style_filter_loc = page.get_by_role('tab', name='Style')
        self.size_filter_loc = page.get_by_role('tab', name='Size')
        self.climate_filter_loc = page.get_by_role('tab', name='Climate')
        self.color_filter_loc = page.get_by_role('tab', name='Color')
        self.eco_collection_filter_loc = page.get_by_role('tab', name='Eco Collection')
        self.erin_recommends_filter_loc = page.get_by_role('tab', name='Erin Recommends')
        self.material_filter_loc = page.get_by_role('tab', name='Material')
        self.new_filter_loc = page.get_by_role('tab', name='New')
        self.pattern_filter_loc = page.get_by_role('tab', name='Pattern')
        self.performance_fabric_filter_loc = page.get_by_role('tab', name='Performance Fabric')
        self.price_filter_loc = page.get_by_role('tab', name='Price')
        self.sale_filter_loc = page.get_by_role('tab', name='Sale')
        self.cart_loc = page.locator('.action.showcart')
        self.cart_proceed_to_checkout_loc = page.locator('#top-cart-btn-checkout')
        self.information_alert_loc = page.locator('[role="alert"]').first