
from generators.base import BaseGenerator
from random import randint


class PythonGenerator(BaseGenerator):

    python_words = [
        # Keywords
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
        'match', 'case',

        # Special Identifiers
        'self', 'cls', '_',

        # Common Built-in Functions
        'print', 'len', 'range', 'type', 'int', 'str', 'list', 'dict', 'set', 'tuple', 'float', 'bool',
        'open', 'input', 'sum', 'min', 'max', 'sorted', 'abs', 'round', 'enumerate', 'zip',
        'map', 'filter', 'reduce', 'any', 'all', 'isinstance', 'issubclass',

        # Common Dunder (Magic) Methods
        '__init__', '__new__', '__str__', '__repr__', '__len__',
        '__call__', '__getitem__', '__setitem__', '__delitem__',
        '__iter__', '__next__', '__enter__', '__exit__',

        # Common Standard Library Modules
        'os', 'sys', 'json', 're', 'datetime', 'math', 'random', 'itertools', 'collections',
        'functools', 'logging', 'threading', 'multiprocessing', 'asyncio', 'pathlib',

        # Symbols and Operators
        '+', '-', '*', '/', '//', '%', '**', '==', '!=', '<', '>', '<=', '>=',
        '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=', 'and', 'or', 'not',
        '&', '|', '^', '~', '<<', '>>', 'in', 'not in', 'is', 'is not',

        # Delimiters
        '(', ')', '[', ']', '{', '}', ':', ';', ',', '.', '...', '_', '@'
    ]

    def get(self, length: int) -> str:
        words_count = len(self.python_words)
        result_string = ''
        while (True):
            rnd = randint(0, words_count - 1)
            result_string += ' ' + self.python_words[rnd]
            if len(result_string) >= length:
                break
        return result_string.lstrip()
