from common.common import get_resource_path
from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class EnglishGenerator(GeneratorABC):

    @property
    def display_name(self): return "English"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _words = []

    def __init__(self) -> None:
        file_name = get_resource_path("src/_content/dictionaries/english.txt")
        with open(file_name, "r", encoding="utf-8") as f:
            self._words = f.read().split()
