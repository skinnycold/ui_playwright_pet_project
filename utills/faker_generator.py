from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.fake = Faker()
        self.email = self.fake.email()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.password = self.fake.password()
