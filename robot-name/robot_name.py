import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        while self.generate_name() == self.name:
            self.name = self.generate_name()

    @staticmethod
    def generate_name():
        letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        digits = random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
        return letters + digits