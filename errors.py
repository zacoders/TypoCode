from collections import defaultdict
from typing import ItemsView


class Errors:

    def __init__(self):
        self.__error_letters = defaultdict(int)
        self.__error_words = defaultdict(int)

    def add_errors(self, letter: str, word: str):

        if letter:
            self.__error_letters[letter] += 1

        if word:
            self.__error_words[word] += 1

        print(f'{self.__error_letters=}')
        print(f'{self.__error_words=}')

    def del_error(self, letter: str, word: str):
        if letter:
            self.__error_letters[letter] -= 1
            if self.__error_letters[letter] <= 0:
                del self.__error_letters[letter]
        if word:
            self.__error_words[word] -= 1
            if self.__error_words[word] <= 0:
                del self.__error_words[word]

        print(f'{self.__error_letters=}')
        print(f'{self.__error_words=}')

    def get_error_letters(self) -> ItemsView[str, int]:
        return self.__error_letters.items()

    def get_error_words(self) -> ItemsView[str, int]:
        return self.__error_words.items()
