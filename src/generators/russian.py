from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class RussianGenerator(GeneratorABC):

    @property
    def display_name(self): return "Русский"

    keyboard_lang = KeyboardLanguage.RUSSIAN

    _words = []

    _level_symbols = [
        set('фывапролджэ '),  # level 0
        set('фывапролджэ йцукенгшщзхъ '),  # level 1
        set('фывапролджэ йцукенгшщзхъ ячсмитьбю'),  # level 2
        set('фывапролджэ йцукенгшщзхъ ячсмитьбю ФЫВАПРОЛДЖЭ ЙЦУКЕНГШЩЗХЪ ЯЧСМИТЬБЮ'),  # level 3
        set('фывапролджэ йцукенгшщзхъ ячсмитьбю ФЫВАПРОЛДЖЭ ЙЦУКЕНГШЩЗХЪ ЯЧСМИТЬБЮ 1234567890'),  # level 4
        set('фывапролджэ йцукенгшщзхъ ячсмитьбю ФЫВАПРОЛДЖЭ ЙЦУКЕНГШЩЗХЪ ЯЧСМИТЬБЮ 1234567890 ёЁ!"№;%:?*()_+-=\\/.,')  # level 5
    ]

    def __init__(self) -> None:
        with open("src/_content/dictionaries/russian.txt", "r", encoding="utf-8") as f:
            self._words = f.read().split()
