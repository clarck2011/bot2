import random
import vk_api

class Cities:
    def __init__(self, user1, user2):
        self.user_ids = [user1, user2]
        self.current_step = random.randint(0, 1)
        self.used_cities = []
        self.last_char = None

    def is_correct_first_char(self, char):
        return self.last_char is None or char == self.last_char

    # ы, ь, ъ

    def is_used_cities(self, city):
        return city in self.used_cities

    def change_last_char(self, city):
        notcorrectchars = ['ы', 'ь']
        for char in city[-1]:
            if city[-1] in notcorrectchars:
                self.last_char = char
                break



