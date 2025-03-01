from playwright.sync_api import Page

class HomePageLocators:
    def __init__(self, page: Page):
        self.title_loc = page.locator('h1')
        self.whats_new_button_loc = page.locator('#ui-id-3')
        self.women_button_loc = page.locator('#ui-id-4')
        self.women_tops_button_loc = page.locator('#ui-id-9')
        self.women_tops_jackets_loc = page.locator('#ui-id-11')
        self.women_tops_hoodies_sweatshirts_loc = page.locator('#ui-id-12')
        self.women_tops_tees_loc = page.locator('#ui-id-13')
        self.women_tops_bras_tanks_loc = page.locator('#ui-id-14')
        self.women_bottoms_button_loc = page.locator('#ui-id-10')
        self.women_bottoms_pants_button_loc = page.locator('#ui-id-15')
        self.women_bottoms_shorts_button_loc = page.locator('#ui-id-16')
        self.men_button_loc = page.locator('#ui-id-5')
        self.men_button_tops_loc = page.locator('#ui-id-17')
        self.men_button_tops_jackets_loc = page.locator('#ui-id-19')
        self.men_button_tops_hoodies_sweatshirts_loc = page.locator('#ui-id-20')
        self.men_button_tops_tees_loc = page.locator('#ui-id-21')
        self.men_button_tops_tanks_loc = page.locator('#ui-id-22')
        self.men_button_bottoms_loc = page.locator('#ui-id-18')
        self.men_button_bottoms_pants_loc = page.locator('#ui-id-23')
        self.men_button_bottoms_shorts_loc = page.locator('#ui-id-24')
        self.gear_button_loc = page.locator('#ui-id-6')
        self.gear_button_bags_loc = page.locator('#ui-id-25')
        self.gear_button_fitness_equipment_loc = page.locator('#ui-id-26')
        self.gear_button_watches_loc = page.locator('#ui-id-27')
        self.training_button_video_download_loc = page.locator('#ui-id-28')
        self.training_button_loc = page.locator('#ui-id-7')
        self.sale_button_loc = page.locator('#ui-id-8')
        self.sign_in_button_loc = page.get_by_role('link', name='Sign In')
        self.create_an_account_button_loc = page.get_by_role('link', name='Create an Account')



