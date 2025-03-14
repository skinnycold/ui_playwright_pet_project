import allure
from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from utills.faker_generator import FakerGenerator

class BasePage:
    url = 'https://magento.softwaretestingboard.com/'
    fg = FakerGenerator()
    current_url = None
    response = None
    cookie_popup = None
    locators = None

    def __init__(self, page: Page):
        self.page = page
        self.email = self.fg.generate_email()
        self.password = self.fg.generate_password()
        self.first_name = self.fg.generate_first_name()
        self.last_name = self.fg.generate_last_name()
        self.street_address = self.fg.generate_street_name()
        self.city = self.fg.generate_city()
        self.postal_code = self.fg.generate_postal_code()
        self.phone_number = self.fg.generate_phone_number()
        self.summary = self.fg.generate_text(20)

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
