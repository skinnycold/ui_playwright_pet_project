from playwright.sync_api import Page

class ProductPageLocators:
    def __init__(self, page: Page):
        self.list_of_prices_loc = page.locator('//*[@data-price-type="finalPrice"]/span')
        self.list_of_products_names_loc = page.locator('.product.name.product-item-name')
        self.list_of_items_loc = page.locator('.item.product.product-item')
        self.grid_mode_button_loc = page.get_by_role('link', name='Grid')
        self.list_mode_button_loc = page.get_by_role('link', name='#mode-list')
        self.sort_selector_loc = page.locator('#sorter').locator('nth=0')
        self.limiter_selector_loc = page.locator('#limiter').locator('nth=1')

        self.category_filter_loc = page.get_by_role('tab', name='Category')
        self.style_filter_loc = page.get_by_role('tab', name='Style')
        self.size_filter_loc = page.get_by_role('tab', name='Size')
        self.climate_filter_loc = page.get_by_role('tab', name='Climate')
        self.eco_collection_filter_loc = page.get_by_role('tab', name='Eco Collection')
        self.erin_recommends_filter_loc = page.get_by_role('tab', name='Erin Recommends')
        self.material_filter_loc = page.get_by_role('tab', name='Material')
        self.new_filter_loc = page.get_by_role('tab', name='New')
        self.pattern_filter_loc = page.get_by_role('tab', name='Pattern')
        self.performance_fabric_filter_loc = page.get_by_role('tab', name='Performance Fabric')
        self.price_filter_loc = page.get_by_role('tab', name='Price')
        self.sale_filter_loc = page.get_by_role('tab', name='Sale')