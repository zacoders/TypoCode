

import pygame
from common.common import is_capslock_on, is_shift_pressed
from generators.keyboard_lang import KeyboardLanguage


class KeyboardService:
    KEYMAP_EN = {
        4: ('a', 'A'), 5: ('b', 'B'), 6: ('c', 'C'), 7: ('d', 'D'),
        8: ('e', 'E'), 9: ('f', 'F'), 10: ('g', 'G'), 11: ('h', 'H'),
        12: ('i', 'I'), 13: ('j', 'J'), 14: ('k', 'K'), 15: ('l', 'L'),
        16: ('m', 'M'), 17: ('n', 'N'), 18: ('o', 'O'), 19: ('p', 'P'),
        20: ('q', 'Q'), 21: ('r', 'R'), 22: ('s', 'S'), 23: ('t', 'T'),
        24: ('u', 'U'), 25: ('v', 'V'), 26: ('w', 'W'), 27: ('x', 'X'),
        28: ('y', 'Y'), 29: ('z', 'Z'),

        30: ('1', '!'), 31: ('2', '@'), 32: ('3', '#'), 33: ('4', '$'),
        34: ('5', '%'), 35: ('6', '^'), 36: ('7', '&'), 37: ('8', '*'),
        38: ('9', '('), 39: ('0', ')'),

        45: ('-', '_'), 46: ('=', '+'), 47: ('[', '{'),
        48: (']', '}'), 49: ('\\', '|'), 51: (';', ':'),
        52: ("'", '"'), 54: (',', '<'), 55: ('.', '>'),
        56: ('/', '?'), 44: (' ', ' '), 53: ('`', '~')
    }

    KEYMAP_RU = {
        4: ('ф', 'Ф'), 5: ('и', 'И'), 6: ('с', 'С'), 7: ('в', 'В'),
        8: ('у', 'У'), 9: ('а', 'А'), 10: ('п', 'П'), 11: ('р', 'Р'),
        12: ('ш', 'Ш'), 13: ('о', 'О'), 14: ('л', 'Л'), 15: ('д', 'Д'),
        16: ('ь', 'Ь'), 17: ('т', 'Т'), 18: ('щ', 'Щ'), 19: ('з', 'З'),
        20: ('й', 'Й'), 21: ('к', 'К'), 22: ('ы', 'Ы'), 23: ('е', 'Е'),
        24: ('г', 'Г'), 25: ('м', 'М'), 26: ('ц', 'Ц'), 27: ('ч', 'Ч'),
        28: ('н', 'Н'), 29: ('я', 'Я'),

        30: ('1', '!'), 31: ('2', '"'), 32: ('3', '№'), 33: ('4', ';'),
        34: ('5', '%'), 35: ('6', ':'), 36: ('7', '?'), 37: ('8', '*'),
        38: ('9', '('), 39: ('0', ')'),

        45: ('-', '_'), 46: ('=', '+'), 47: ('х', 'Х'),
        48: ('ъ', 'Ъ'), 49: ('\\', '/'), 51: ('ж', 'Ж'),
        52: ('э', 'Э'), 54: ('б', 'Б'), 55: ('ю', 'Ю'),
        56: ('.', ','), 44: (' ', ' '), 53: ('ё', 'Ё')
    }

    def get_char_from_key(self, scancode: int, keyboard_lang: KeyboardLanguage) -> str:
        is_capslock = is_capslock_on()
        is_shift = is_shift_pressed()
        is_upper = is_capslock ^ is_shift

        char = ''
        keymap = {}

        if keyboard_lang == KeyboardLanguage.ENGLISH:
            keymap = self.KEYMAP_EN
        elif keyboard_lang == KeyboardLanguage.RUSSIAN:
            keymap = self.KEYMAP_RU

        if scancode in keymap:
            if is_shift:
                char = keymap[scancode][1]
            else:
                char = keymap[scancode][0]
            if is_upper:
                return char.upper()
            else:
                return char.lower()

        raise Exception("Symbol is not found in the KEYMAP.")
