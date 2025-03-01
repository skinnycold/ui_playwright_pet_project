from playwright.sync_api import Page, expect


class BasePage:
    url = 'https://magento.softwaretestingboard.com/'
    current_url = None
    response = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.current_url:
            self.page.goto(self.url + self.current_url)
        else:
            raise NotImplementedError('Where is your current page????')

    def wait_full_load_page(self):
        self.page.wait_for_load_state('networkidle', timeout=30000)

    def check_title(self, title_text: str):
        assert self.page.title() == title_text, f"Фактический titile: {self.page.title(),} Ожидаемый title: {title_text}"

