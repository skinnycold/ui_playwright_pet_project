import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    current_url = ''

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomePageLocators(page)

    def open(self):
        with allure.step(f"Переход на страницу: {self.url + self.current_url}"):
            self.page.goto(self.url)

    def press_whats_new_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.whats_new_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.whats_new_button_loc.get_attribute('href')}")
            self.locators.whats_new_button_loc.click()

    def press_women_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.women_button_loc.get_attribute('href')}")
            self.locators.women_button_loc.click()

    def press_women_tops_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_tops_button_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            allure.attach(f"{self.locators.women_tops_button_loc.get_attribute('href')}")
            self.locators.women_tops_button_loc.click()

    def press_women_tops_jackets_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_tops_jackets_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_tops_button_loc.hover()
            allure.attach(f"{self.locators.women_tops_jackets_loc.get_attribute('href')}")
            self.locators.women_tops_jackets_loc.click()

    def press_women_tops_hoodies_sweatshirts_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_tops_hoodies_sweatshirts_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_tops_button_loc.hover()
            allure.attach(f"{self.locators.women_tops_hoodies_sweatshirts_loc.get_attribute('href')}")
            self.locators.women_tops_hoodies_sweatshirts_loc.click()

    def press_women_tops_tees_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_tops_tees_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_tops_button_loc.hover()
            allure.attach(f"{self.locators.women_tops_tees_loc.get_attribute('href')}")
            self.locators.women_tops_tees_loc.click()

    def press_women_tops_bras_tanks_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_tops_bras_tanks_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_tops_button_loc.hover()
            allure.attach(f"{self.locators.women_tops_bras_tanks_loc.get_attribute('href')}")
            self.locators.women_tops_bras_tanks_loc.click()

    def press_women_bottoms_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_bottoms_button_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            allure.attach(f"{self.locators.women_bottoms_button_loc.get_attribute('href')}")
            self.locators.women_bottoms_button_loc.click()

    def press_women_bottoms_pants_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_bottoms_pants_button_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_bottoms_button_loc.hover()
            allure.attach(f"{self.locators.women_bottoms_pants_button_loc.get_attribute('href')}")
            self.locators.women_bottoms_pants_button_loc.click()

    def press_women_bottoms_shorts_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.women_bottoms_shorts_button_loc.inner_text()}"):
            self.locators.women_button_loc.hover()
            self.locators.women_bottoms_button_loc.hover()
            allure.attach(f"{self.locators.women_bottoms_shorts_button_loc.get_attribute('href')}")
            self.locators.women_bottoms_shorts_button_loc.click()

    def press_men_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.men_button_loc.get_attribute('href')}")
            self.locators.men_button_loc.click()

    def press_men_tops_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_tops_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            allure.attach(f"{self.locators.men_button_tops_loc.get_attribute('href')}")
            self.locators.men_button_tops_loc.click()

    def press_men_tops_jackets_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_tops_jackets_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_tops_loc.hover()
            allure.attach(f"{self.locators.men_button_tops_jackets_loc.get_attribute('href')}")
            self.locators.men_button_tops_jackets_loc.click()

    def press_men_tops_jackets_hoodies_sweatshirts_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_tops_hoodies_sweatshirts_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_tops_loc.hover()
            allure.attach(f"{self.locators.men_button_tops_hoodies_sweatshirts_loc.get_attribute('href')}")
            self.locators.men_button_tops_hoodies_sweatshirts_loc.click()

    def press_men_tops_jackets_tees_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_tops_tees_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_tops_loc.hover()
            allure.attach(f"{self.locators.men_button_tops_tees_loc.get_attribute('href')}")
            self.locators.men_button_tops_tees_loc.click()

    def press_men_tops_jackets_tanks_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_tops_tanks_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_tops_loc.hover()
            allure.attach(f"{self.locators.men_button_tops_tanks_loc.get_attribute('href')}")
            self.locators.men_button_tops_tanks_loc.click()

    def press_men_bottoms_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_bottoms_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            allure.attach(f"{self.locators.men_button_bottoms_loc.get_attribute('href')}")
            self.locators.men_button_bottoms_loc.click()

    def press_men_bottoms_pants_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_bottoms_pants_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_bottoms_loc.hover()
            allure.attach(f"{self.locators.men_button_bottoms_pants_loc.get_attribute('href')}")
            self.locators.men_button_bottoms_pants_loc.click()

    def press_men_bottoms_shorts_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.men_button_bottoms_shorts_loc.inner_text()}"):
            self.locators.men_button_loc.hover()
            self.locators.men_button_bottoms_loc.hover()
            allure.attach(f"{self.locators.men_button_bottoms_shorts_loc.get_attribute('href')}")
            self.locators.men_button_bottoms_shorts_loc.click()

    def press_gear_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.gear_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.gear_button_loc.get_attribute('href')}")
            self.locators.gear_button_loc.click()

    def press_gear_bags_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.gear_button_bags_loc.inner_text()}"):
            self.locators.gear_button_loc.hover()
            allure.attach(f"{self.locators.gear_button_bags_loc.get_attribute('href')}")
            self.locators.gear_button_bags_loc.click()

    def press_gear_fitness_equipment_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.gear_button_fitness_equipment_loc.inner_text()}"):
            self.locators.gear_button_loc.hover()
            allure.attach(f"{self.locators.gear_button_fitness_equipment_loc.get_attribute('href')}")
            self.locators.gear_button_fitness_equipment_loc.click()

    def press_gear_watches_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.gear_button_watches_loc.inner_text()}"):
            self.locators.gear_button_loc.hover()
            allure.attach(f"{self.locators.gear_button_watches_loc.get_attribute('href')}")
            self.locators.gear_button_watches_loc.click()

    def press_training_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.training_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.training_button_loc.get_attribute('href')}")
            self.locators.training_button_loc.click()

    def press_training_video_download_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.training_button_video_download_loc.inner_text()}"):
            self.locators.training_button_loc.hover()
            allure.attach(f"{self.locators.training_button_video_download_loc.get_attribute('href')}")
            self.locators.training_button_video_download_loc.click()

    def press_sale(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.sale_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.sale_button_loc.get_attribute('href')}")
            self.locators.sale_button_loc.click()

    def press_sign_in_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.sign_in_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.sign_in_button_loc.get_attribute('href')}")
            self.locators.sign_in_button_loc.click()

    def press_create_an_account_button(self):
        with allure.step(f"Нажимаем на кнопку: {self.locators.create_an_account_button_loc.inner_text()}"):
            allure.attach(f"{self.locators.create_an_account_button_loc.get_attribute('href')}")
            self.locators.create_an_account_button_loc.click()
