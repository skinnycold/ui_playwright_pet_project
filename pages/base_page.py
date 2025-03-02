from playwright.sync_api import Page, expect
from playwright.sync_api import  TimeoutError as PlaywrightTimeoutError

class BasePage:
    url = 'https://magento.softwaretestingboard.com/'
    current_url = None
    response = None
    cookie_popup = None
    locators = None
    product_page_locators = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.current_url:
            self.page.goto(self.url + self.current_url)
        else:
            raise NotImplementedError('Where is your current page????')

    def agree_cookie(self):
        self.cookie_popup = self.page.locator('.css-1n36tvh')
        try:
            self.cookie_popup.wait_for(state="visible", timeout=2000)
            self.cookie_popup.click()
        except PlaywrightTimeoutError:
            pass

    def wait_full_load_page(self):
        self.page.wait_for_load_state('load', timeout=30000)

    def check_title(self, title_text: str):
        expect(self.page).to_have_title(title_text, timeout=3000)

    def check_h1(self, title_text):
        expect(self.page.locator('h1')).to_have_text(title_text, timeout=3000)



