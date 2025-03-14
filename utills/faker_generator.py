from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_email(self):
        return self.fake.email()

    def generate_first_name(self):
        return self.fake.first_name()

    def generate_last_name(self):
        return self.fake.last_name()

    def generate_password(self):
        return self.fake.password()

    def generate_text(self, quantity_char:int = 20):
        return self.fake.text(quantity_char)

    def generate_street_name(self):
        return self.fake.street_name()

    def generate_city(self):
        return self.fake.city()

    def generate_postal_code(self):
        return self.fake.postalcode()

    def generate_phone_number(self):
        return self.fake.basic_phone_number()

