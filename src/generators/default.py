

import random
import string
from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class RandomGenerator(GeneratorABC):

    @property
    def display_name(self): return "English Random"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _words = []

    def __init__(self) -> None:
        text = ""
        word_len = random.randint(1, 10)
        for _ in range(100):
            random_char = random.choice(string.ascii_lowercase)

            if len(text) < word_len:
                text += random_char
            else:
                self._words.append(text)
                word_len = random.randint(1, 10)
                text = ""
