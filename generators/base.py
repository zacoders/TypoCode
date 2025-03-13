
from abc import ABC
from errors import Errors
import random

from generators.keyboard_lang import KeyboardLanguage


class BaseGenerator(ABC):

    keyboard_lang = KeyboardLanguage.ENGLISH

    _words = []

    def get_text(self, length: int, errors: Errors) -> str:
        text = ''
        while True:
            total_len = len(text)
            if total_len >= length:
                break

            max_word_len = length - total_len - 1

            word_type = random.random()
            error_words = errors.get_error_words()
            error_letters = errors.get_error_letters()

            if max_word_len == 0:
                word = self._get_random_word(words=self._words, max_length=1)
                text += word
                continue
            elif word_type < 0.1:
                word = self._get_random_number(max_word_len)
            elif word_type < 0.5 and len(error_words) > 0:
                word = self._get_random_word(words=error_words, max_length=max_word_len)
                if not word:
                    continue
                errors.del_word(word)
            elif word_type < 0.75 and len(error_words) == 0 and len(error_letters) > 0:
                rand_letter = random.choice(error_letters)
                word = self._get_random_word_with_letter(words=self._words, max_length=max_word_len)
                if not word:
                    continue
                errors.del_letter(rand_letter)
            else:
                word = self._get_random_word(words=self._words, max_length=max_word_len)

            text += ' ' + word
            text = text.lstrip()

        return text

    def _get_random_word(self, words: list[str], max_length: int = 999):
        right_words = list(filter(lambda w: len(w) <= max_length, words))
        if len(right_words) == 0:
            return ''
        return random.choice(list(right_words))

    def _get_random_word_with_letter(self, words: list[str], max_length: int = 999, letter: str = ''):
        right_words = filter(
            lambda w: len(w) <= max_length and letter in w,
            words
        )
        return random.choice(list(right_words))

    def _get_random_number(self, max_length: int) -> str:
        if max_length > 10:
            max_length = 10
        max_length = random.randint(1, max_length)
        return str(random.randint(0, 10 ** max_length - 1))
