from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.fake = Faker()
        self.email = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.text = None
        self.street_name = None
        self.city = None
        self.postal_code = None
        self.phone_number = None

    def generate_email(self):
        self.email = self.fake.email()
        return self.email

    def generate_first_name(self):
        self.first_name = self.fake.first_name()
        return self.first_name

    def generate_last_name(self):
        self.last_name = self.fake.last_name()
        return self.last_name

    def generate_password(self):
        self.password = self.fake.password()
        return self.password

    def generate_text(self, quantity_char:int = 20):
        self.text = self.fake.text(quantity_char)
        return self.text

    def generate_street_name(self):
        self.street_name = self.fake.street_name()
        return self.street_name

    def generate_city(self):
        self.city = self.fake.city()
        return self.city

    def generate_postal_code(self):
        self.postal_code = self.fake.postalcode()
        return self.postal_code

    def generate_phone_number(self):
        self.phone_number = self.fake.basic_phone_number()
        return self.phone_number

