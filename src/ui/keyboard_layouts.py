
from generators.keyboard_lang import KeyboardLanguage


class KeyboardLayouts:

    ENG_UPPER = [
        "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "<--",
        "Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|",
        "Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '"', "Enter",
        "L-Shift", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    ENG_LOWER = [
        "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "<--",
        "Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
        "Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "Enter",
        "L-Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    RUS_UPPER = [
        "Ё", "!", '"', "Nº", ";", "%", ":", "?", "*", "(", ")", "_", "+", "<--",
        "Tab", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "/",
        "Caps", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Enter",
        "L-Shift", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ",", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    RUS_LOWER = [
        "ё", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "<--",
        "Tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "\\",
        "Caps", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "Enter",
        "L-Shift", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".", "R-Shift",
        "Ctrl", "Win", "Alt", "Space", "Alt", "Fn", "Menu", "Ctrl"
    ]

    @classmethod
    def get_layout(cls, lang: KeyboardLanguage):
        if lang == KeyboardLanguage.ENGLISH:
            return cls.ENG_LOWER, cls.ENG_UPPER
        elif lang == KeyboardLanguage.RUSSIAN:
            return cls.RUS_LOWER, cls.RUS_UPPER
        raise Exception(f"Unknown language {lang}")
