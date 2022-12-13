import os
from dataclasses import dataclass

import faker
from PIL import Image

fake = faker.Faker('ru_RU')


class DataManager:

    def __init__(self, path):
        self.path = path

    @staticmethod
    def user(email=None, name=None, phone=None, town=None, bio=None):
        @dataclass
        class User:
            email: str
            name: str
            phone: int
            town: str
            bio: str

        return User(
            email=email if email is not None else fake.email(),
            name=name or fake.name(),
            phone=phone or fake.phone_number(),
            town=town or fake.city(),
            bio=bio or fake.bothify(text='????? ?? ?? ?????? ??? ???? #########')
        )

    def image(self, name=None, width=100, height=100, color=None):
        if name is None:
            name = fake.lexify('????????.png')

        path = os.path.join(self.path, name)

        img = Image.new('RGB', (width, height), color=color or fake.color())
        img.save(path)

        return img, path
