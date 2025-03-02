from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators
from playwright.sync_api import Page, expect

class HomePage(BasePage):
    current_url = ''

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomePageLocators(page)

    def open(self):
        self.page.goto(self.url)

    def press_whats_new_button(self):
        self.locators.whats_new_button_loc.click()

    def press_women_button(self):
        self.locators.women_button_loc.click()

    def press_women_tops_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_tops_button_loc.click()

    def press_women_tops_jackets_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_tops_button_loc.hover()
        self.locators.women_tops_jackets_loc.click()

    def press_women_tops_hoodies_sweatshirts_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_tops_button_loc.hover()
        self.locators.women_tops_hoodies_sweatshirts_loc.click()

    def press_women_tops_tees_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_tops_button_loc.hover()
        self.locators.women_tops_tees_loc.click()

    def press_women_tops_bras_tanks_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_tops_button_loc.hover()
        self.locators.women_tops_bras_tanks_loc.click()

    def press_women_bottoms_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_bottoms_button_loc.click()

    def press_women_bottoms_pants_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_bottoms_button_loc.hover()
        self.locators.women_bottoms_pants_button_loc.click()

    def press_women_bottoms_shorts_button(self):
        self.locators.women_button_loc.hover()
        self.locators.women_bottoms_button_loc.hover()
        self.locators.women_bottoms_shorts_button_loc.click()

    def press_men_button(self):
        self.locators.men_button_loc.click()

    def press_men_tops_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_tops_loc.click()

    def press_men_tops_jackets_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_tops_loc.hover()
        self.locators.men_button_tops_jackets_loc.click()

    def press_men_tops_jackets_hoodies_sweatshirts_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_tops_loc.hover()
        self.locators.men_button_tops_hoodies_sweatshirts_loc.click()

    def press_men_tops_jackets_tees_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_tops_loc.hover()
        self.locators.men_button_tops_tees_loc.click()

    def press_men_tops_jackets_tanks_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_tops_loc.hover()
        self.locators.men_button_tops_tanks_loc.click()

    def press_men_bottoms_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_bottoms_loc.click()

    def press_men_bottoms_pants_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_bottoms_loc.hover()
        self.locators.men_button_bottoms_pants_loc.click()

    def press_men_bottoms_shorts_button(self):
        self.locators.men_button_loc.hover()
        self.locators.men_button_bottoms_loc.hover()
        self.locators.men_button_bottoms_shorts_loc.click()

    def press_gear_button(self):
        self.locators.gear_button_loc.click()

    def press_gear_bags_button(self):
        self.locators.gear_button_loc.hover()
        self.locators.gear_button_bags_loc.click()

    def press_gear_fitness_equipment_button(self):
        self.locators.gear_button_loc.hover()
        self.locators.gear_button_fitness_equipment_loc.click()

    def press_gear_watches_button(self):
        self.locators.gear_button_loc.hover()
        self.locators.gear_button_watches_loc.click()

    def press_training_button(self):
        self.locators.training_button_loc.click()

    def press_training_video_download_button(self):
        self.locators.training_button_loc.hover()
        self.locators.training_button_video_download_loc.click()

    def press_sale(self):
        self.locators.sale_button_loc.click()

    def press_sign_in_button(self):
        self.locators.sign_in_button_loc.click()

    def press_create_an_account_button(self):
        self.locators.create_an_account_button_loc.click()
