from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class RussianGenerator(GeneratorABC):

    @property
    def display_name(self): return "Русский"

    keyboard_lang = KeyboardLanguage.RUSSIAN

    _words = []

    def __init__(self) -> None:
        with open("src/_content/dictionaries/russian.txt", "r", encoding="utf-8") as f:
            self._words = f.read().split()
