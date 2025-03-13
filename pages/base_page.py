import allure
from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class BasePage:
    url = 'https://magento.softwaretestingboard.com/'
    current_url = None
    response = None
    cookie_popup = None
    locators = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """
        Осуществляет переход на страницу по current_url экземпляра
        """
        if self.current_url:
            with allure.step(f"Переход на страницу: {self.url + self.current_url}"):
                self.page.goto(self.url + self.current_url)
                self.page.wait_for_load_state("load")
        else:
            raise NotImplementedError('Where is your current page????')

    def agree_cookie(self):
        """
        Соглашается с куки-файлами, если нужно
        """
        self.cookie_popup = self.page.locator('.css-1n36tvh')
        try:
            with allure.step("Принимаем соглашение об использовании Cookie"):
                self.cookie_popup.wait_for(state="visible", timeout=20000)
                self.cookie_popup.click()
        except PlaywrightTimeoutError:
            pass

    def wait_full_load_page(self):
        """
        Ожидание полной загрузки файлов
        """
        self.page.wait_for_load_state('load', timeout=30000)

    def check_title(self, title_text: str):
        """
         Проверяет title страницы
        :param title_text: Title страницы
        """
        with allure.step(f"Проверяем заголовок страницы"):
            allure.attach(f"Ожидаемый заголовок: {title_text}")
            allure.attach(f"Фактический заголовок: {self.page.title()}")
            expect(self.page).to_have_title(title_text, timeout=30000)

    def check_h1(self, title_text):
        """
        Проверяет заголовок H1
        :param title_text: H1 заголовок
        """
        with allure.step(f"Проверяем H1 заголовок страницы"):
            allure.attach(f"Ожидаемый H1 заголовок: {title_text}")
            allure.attach(f"Фактический H1 заголовок: {self.page.locator('h1').inner_text()}")
            expect(self.page.locator('h1')).to_have_text(title_text, timeout=30000)
