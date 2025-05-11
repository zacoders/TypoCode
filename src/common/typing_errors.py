from collections import defaultdict
from typing import List


class TypingErrors:

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
        

    def del_word(self, word: str):
        if word:
            self.__error_words[word] -= 1
            if self.__error_words[word] <= 0:
                del self.__error_words[word]

        print(f'{self.__error_words=}')

    def del_letter(self, letter: str):
        if letter:
            self.__error_letters[letter] -= 1
            if self.__error_letters[letter] <= 0:
                del self.__error_letters[letter]
        print(f'{self.__error_letters=}')

    def get_error_letters(self) -> List[str]:
        return list(self.__error_letters.keys())

    def get_error_words(self) -> List[str]:
        return list(self.__error_words.keys())
