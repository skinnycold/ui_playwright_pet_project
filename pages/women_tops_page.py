from pages.base_page import BasePage

class WomenTopsPage(BasePage):
    current_url = '/women/tops-women.html'

    def __init__(self, page):
        super().__init__(page)