
class Errors:

    def __init__(self):
        self.__error_letters = {}
        self.__error_words = {}

    def add_errors(self, current_letter: str, current_word: str):

        if current_letter in self.__error_letters:
            self.__error_letters[current_letter] += 1
        else:
            self.__error_letters[current_letter] = 1

        if current_word in self.__error_words:
            self.__error_letters[current_letter] += 1
        else:
            self.__error_words[current_word] = 1

    def get_error_letters(self):
        return self.__error_letters

    def get_error_words(self):
        return self.__error_words
