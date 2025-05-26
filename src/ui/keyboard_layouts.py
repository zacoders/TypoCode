
from typing import List
from generators.keyboard_lang import KeyboardLanguage
from functools import cache


class KeyboardLayouts:

    ENG_MAIN = [
        "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "<--",
        "Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
        "Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "Enter",
        "L-Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    ENG_SHIFT = [
        "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "<--",
        "Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "{", "}", "|",
        "Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ":", '"', "Enter",
        "L-Shift", "z", "x", "c", "v", "b", "n", "m", "<", ">", "?", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    RUS_MAIN = [
        "ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "<--",
        "Tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "\\",
        "Caps", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "Enter",
        "L-Shift", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    RUS_SHIFT = [
        "ё", "!", '"', "Nº", ";", "%", ":", "?", "*", "(", ")", "_", "+", "<--",
        "Tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "/",
        "Caps", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "Enter",
        "L-Shift", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ",", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    @classmethod
    @cache
    def get_layout(cls, lang: KeyboardLanguage, is_shift: bool, is_capslock: bool) -> List[str]:
        if lang == KeyboardLanguage.ENGLISH:
            return list(cls._get_layout_internal(cls.ENG_MAIN, cls.ENG_SHIFT, is_shift, is_capslock))
        elif lang == KeyboardLanguage.RUSSIAN:
            return list(cls._get_layout_internal(cls.RUS_MAIN, cls.RUS_SHIFT, is_shift, is_capslock))
        raise Exception(f"Unknown language {lang}")

    @classmethod
    def _get_layout_internal(cls, main_layout: List[str], shift_layout: List[str], is_shift: bool, is_capslock: bool):
        layout = shift_layout if is_shift else main_layout
        for c in layout:
            if len(c) == 1 and c.isalpha():
                if is_shift ^ is_capslock:
                    yield c.upper()
                else:
                    yield c.lower()
            else:
                yield c
