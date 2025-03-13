

import random
import string
from generators.base import BaseGenerator
from generators.keyboard_lang import KeyboardLanguage


class RandomGenerator(BaseGenerator):

    keyboard_lang = KeyboardLanguage.ENGLISH

    def get_text(self, len: int) -> str:
        result = ''
        for _ in range(len):
            random_char = random.choice(string.ascii_lowercase)
            result += random_char

        return result
