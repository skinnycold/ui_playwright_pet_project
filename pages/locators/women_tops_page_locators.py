from playwright.sync_api import Page

class WomenTopsPageLocators:
    def __init__(self, page: Page):
        self.category_jackets_filter_log = page.get_by_role('link', name='Jackets')
        self.category_hoodies_sweatshirts_filter_log = page.get_by_role('link', name='Hoodies & Sweatshirts')
        self.category_tees_filter_log = page.get_by_role('link', name='Tees')
        self.category_bras_tanks_filter_log = page.get_by_role('link', name='Bras & Tanks')

        self.style_insulated_filter_log = page.get_by_role('link', name='Insulated')
        self.style_jacket_filter_log = page.get_by_role('link', name='Jacket')
        self.style_lightweight_filter_log = page.get_by_role('link', name='Lightweight')
        self.style_hooded_filter_log = page.get_by_role('link', name='Hooded')
        self.style_heavy_duty_filter_log = page.get_by_role('link', name='Heavy Duty')
        self.style_rain_coat_filter_log = page.get_by_role('link', name='Rain Coat')
        self.style_hard_shell_filter_log = page.get_by_role('link', name='Hard Shell')
        self.style_soft_shell_filter_log = page.get_by_role('link', name='Soft Shell')
        self.style_windbreaker_filter_log = page.get_by_role('link', name='Windbreaker')
        self.style_1_4_zip_filter_log = page.get_by_role('link', name='¼ zip')
        self.style_full_zip_filter_log = page.get_by_role('link', name='Full Zip')
        self.style_reversible_filter_log = page.get_by_role('link', name='Reversible')
        self.style_bra_filter_log = page.get_by_role('link', name='Bra')
        self.style_sweatshirt_filter_log = page.get_by_role('link', name='Sweatshirt')
        self.style_tank_filter_log = page.get_by_role('link', name='Tank')
        self.style_tee_filter_log = page.get_by_role('link', name='Tee')
        self.style_hoodie_filter_log = page.get_by_role('link', name='Hoodie')
        self.style_camisole_filter_log = page.get_by_role('link', name='Camisole')

        self.size_xs_filter_log = page.locator('[class="swatch-option-link-layered"] div[option-label="XS"]')
        self.size_s_filter_log = page.locator('[class="swatch-option-link-layered"] div[option-label="S"]')
        self.size_m_filter_log = page.locator('[class="swatch-option-link-layered"] div[option-label="M"]')
        self.size_l_filter_log = page.locator('[class="swatch-option-link-layered"] div[option-label="L"]')
        self.size_xl_filter_log = page.locator('[class="swatch-option-link-layered"] div[option-label="XL"]')

        self.climate_all_weather_filter_log = page.get_by_role('link', name='All-Weather')
        self.climate_cold_filter_log = page.get_by_role('link', name='Cold')
        self.climate_cool_filter_log = page.get_by_role('link', name='Cool')
        self.climate_indoor_filter_log = page.get_by_role('link', name='Indoor')
        self.climate_mild_filter_log = page.get_by_role('link', name='Mild')
        self.climate_rainy_filter_log = page.get_by_role('link', name='Rainy')
        self.climate_spring_filter_log = page.get_by_role('link', name='Spring')
        self.climate_warm_filter_log = page.get_by_role('link', name='Warm')
        self.climate_windy_filter_log = page.get_by_role('link', name='Windy')
        self.climate_wintry_filter_log = page.get_by_role('link', name='Windy')

        self.color_black_filter_log = page.locator('a[aria-label="Black"] div[option-label="Black"]')
        self.color_blue_filter_log = page.locator('a[aria-label="Blue"] div[option-label="Blue"]')
        self.color_brown_filter_log = page.locator('a[aria-label="Brown"] div[option-label="Brown"]')
        self.color_gray_filter_log = page.locator('a[aria-label="Gray"] div[option-label="Gray"]')
        self.color_green_filter_log = page.locator('a[aria-label="Green"] div[option-label="Green"]')
        self.color_orange_filter_log = page.locator('a[aria-label="Orange"] div[option-label="Orange"]')
        self.color_purple_filter_log = page.locator('a[aria-label="Purple"] div[option-label="Purple"]')
        self.color_red_filter_log = page.locator('a[aria-label="Red"] div[option-label="Red"]')
        self.color_white_filter_log = page.locator('a[aria-label="White"] div[option-label="White"]')
        self.color_yellow_filter_log = page.locator('a[aria-label="Yellow"] div[option-label="Yellow"]')

        self.eco_collection_yes_filter_log = page.get_by_role('link', name='Yes')
        self.eco_collection_no_filter_log = page.get_by_role('link', name='No')

        self.erin_recommends_yes_filter_log = page.get_by_role('link', name='Yes')
        self.erin_recommends_no_filter_log = page.get_by_role('link', name='No')

        self.material_cocona_performance_fabric_filter_log = page.get_by_role(
            'link', name='Cocona® performance fabric'
        )
        self.material_cotton_filter_log = page.get_by_role('link', name='Cotton')
        self.material_fleece_filter_log = page.get_by_role('link', name='Fleece')
        self.material_hemp_filter_log = page.get_by_role('link', name='Hemp')
        self.material_jersey_filter_log = page.get_by_role('link', name='Jersey')
        self.material_lumatech_filter_log = page.get_by_role('link', name='LumaTech™')
        self.material_mesh_filter_log = page.get_by_role('link', name='Mesh')
        self.material_lycra_filter_log = page.get_by_role('link', name='Lycra®')
        self.material_nylon_filter_log = page.get_by_role('link', name='Nylon')
        self.material_microfiber_filter_log = page.get_by_role('link', name='Microfiber')
        self.material_polyester_filter_log = page.get_by_role('link', name='Polyester')
        self.material_spandex_filter_log = page.get_by_role('link', name='Spandex')
        self.material_heattec_filter_log = page.get_by_role('link', name='HeatTec®')
        self.material_evercool_filter_log = page.get_by_role('link', name='EverCool™')
        self.material_organic_cotton_filter_log = page.get_by_role('link', name='Organic Cotton')
        self.material_tencel_filter_log = page.get_by_role('link', name='TENCEL')
        self.material_cooltech_filter_log = page.get_by_role('link', name='CoolTech™')
        self.material_wool_filter_log = page.get_by_role('link', name='Wool')

        self.new_yes_filter_log = page.get_by_role('link', name='Yes')
        self.new_no_filter_log = page.get_by_role('link', name='No')

        self.pattern_checked_filter_log = page.get_by_role('link', name='Checked')
        self.pattern_color_blocked_filter_log = page.get_by_role('link', name='Color-Blocked')
        self.pattern_solid_filter_log = page.get_by_role('link', name='Solid')
        self.pattern_striped_filter_log = page.get_by_role('link', name='Striped')

        self.performance_fabric_yes_filter_log = page.get_by_role('link', name='Yes')
        self.performance_fabric_no_filter_log = page.get_by_role('link', name='No')

        self.price_20_29_filter_log = page.get_by_role('link', name='$20.00')
        self.price_30_39_filter_log = page.get_by_role('link', name='$30.00')
        self.price_40_49_filter_log = page.get_by_role('link', name='$40.00')
        self.price_50_59_filter_log = page.get_by_role('link', name='$50.00')
        self.price_60_69_filter_log = page.get_by_role('link', name='$60.00')
        self.price_70_79_filter_log = page.get_by_role('link', name='$70.00')
        self.price_80_above_filter_log = page.get_by_role('link', name='$80.00')

        self.sale_yes_filter_log = page.get_by_role('link', name='Yes')
        self.sale_no_filter_log = page.get_by_role('link', name='No')





        """
        надо писать все локаторы фильтров на странице
        """