from generators.base import BaseGenerator
from generators.keyboard_lang import KeyboardLanguage


class EnglishGenerator(BaseGenerator):

    @property
    def display_name(self): return "English"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _words = []

    def __init__(self) -> None:
        with open("dictionaries/english.txt", "r", encoding="utf-8") as f:
            self._words = f.read().split()
