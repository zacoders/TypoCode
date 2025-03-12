from generators.base import BaseGenerator


class EnglishGenerator(BaseGenerator):
    _words = []

    def __init__(self) -> None:
        with open("dictionaries/english.txt", "r", encoding="utf-8") as f:
            self._words = f.read().split()
