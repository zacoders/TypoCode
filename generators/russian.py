from generators.base import BaseGenerator
from generators.keyboard_lang import KeyboardLanguage


class RussianGenerator(BaseGenerator):

    keyboard_lang = KeyboardLanguage.RUSSIAN
    
    _words = []

    def __init__(self) -> None:
        with open("dictionaries/russian.txt", "r", encoding="utf-8") as f:
            self._words = f.read().split()
