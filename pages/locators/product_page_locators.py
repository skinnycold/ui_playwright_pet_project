from playwright.sync_api import Page

class ProductPageLocators:
    def __init__(self, page: Page):
        self.list_of_prices_loc = page.locator('//*[@data-price-type="finalPrice"]/span')
        self.grid_mode_button_loc = page.get_by_role('link', name='Grid')
        self.list_mode_button_loc = page.get_by_role('link', name='#mode-list')
        self.sort_selector_loc = page.locator('#sorter').locator('nth=0')
        self.limiter_selector_loc = page.locator('##limiter').locator('nth=1')
