import pytest
from unittest.mock import MagicMock

from typing_errors import TypingErrors
from generators.python import PythonGenerator


def test_get_random_word():

    gen = PythonGenerator()
    words = ['database', 'generator', 'len']

    for _ in range(1, 100):
        word = gen._get_random_word(words, 5, 5)
        assert len(word) <= 5
        assert word == 'len'


def test_get_single():

    gen = PythonGenerator()

    text = gen.get_text(32, TypingErrors(), 5)
    assert len(text) == 32


def test_get_multiple():

    gen = PythonGenerator()

    for _ in range(1, 500):
        text = gen.get_text(32, TypingErrors(), 5)
        assert len(text) == 32


def test_get1():

    gen = PythonGenerator()
    gen._get_random_word = MagicMock(side_effect=["333", "55555", "22", "333"])

    text = gen.get_text(16, TypingErrors(), 5)

    assert text == '333 55555 22 333'
    assert len(text) == 16
