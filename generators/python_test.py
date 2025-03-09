import pytest
from unittest.mock import MagicMock

from generators.python import PythonGenerator


def test_get_random_word():

    gen = PythonGenerator()

    for _ in range(1, 100):
        word = gen._get_random_word(1, 5)
        assert len(word) >= 1
        assert len(word) <= 5


def test_get_single():

    gen = PythonGenerator()

    text = gen.get(32)
    assert len(text) == 32


def test_get_multiple():

    gen = PythonGenerator()

    for _ in range(1, 500):
        text = gen.get(32)
        assert len(text) == 32


def test_get1():

    gen = PythonGenerator()
    gen._get_random_word = MagicMock(side_effect=["333", "55555", "22", "333"])

    text = gen.get(16)

    assert text == '333 55555 22 333'
    assert len(text) == 16


# def test_get2():

#     gen = PythonGenerator()
#     gen._get_random_word = MagicMock(side_effect=["333", "55555", "55555", '1'])

#     text = gen.get(16)

#     assert text == '333 55555 555551'
#     assert len(text) == 16
