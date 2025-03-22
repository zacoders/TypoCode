
import pygame
from pygame.event import Event
from pygame.key import ScancodeWrapper
from common.common import is_capslock_on, is_shift_pressed
from generators.keyboard_lang import KeyboardLanguage
from random import randint


class Keyboard:

    KEY_SIZE = 40.0
    KEY_SPACING = 6.0
    FONT_SIZE = 24.0
    LINE_KEYS_COUNT = 15
    SIZE = 0.7  # 70% of the screen

    def __init__(self, language: KeyboardLanguage):
        self.__x = 0
        self.__y = 0
        self.__keys = {}
        self.__highlighted_key = None
        self.__screen_height = -1
        self.__screen_width = -1
        self.__language = language
        self.__is_upper_case = False

        self.__eng_layout_uppercase = [
            [("~", 1), ("!", 1), ("@", 1), ("#", 1), ("$", 1), ("%", 1), ("^", 1),
             ("&", 1), ("*", 1), ("(", 1), (")", 1), ("_", 1), ("+", 1), ("<--", 2)],

            [("Tab", 1.5), ("q", 1), ("w", 1), ("e", 1), ("r", 1), ("t", 1), ("y", 1),
             ("u", 1), ("i", 1), ("o", 1), ("p", 1), ("[", 1), ("]", 1), ("\\", 1.5)],

            [("CAPS", 1.8), ("a", 1), ("s", 1), ("d", 1), ("f", 1), ("g", 1),
             ("h", 1), ("j", 1), ("k", 1), ("l", 1), (";", 1), ("'", 1), ("ENTER", 2.35)],

            [("SHIFT", 2.30), ("z", 1), ("x", 1), ("c", 1), ("v", 1), ("b", 1),
             ("n", 1), ("m", 1), (",", 1), (".", 1), ("/", 1), ("Shift", 3.0)],

            [("CTRL", 1.25), ("Win", 1.25), ("ALT", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__eng_layout_lowercase = [
            [("`", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
             ("7", 1), ("8", 1), ("9", 1), ("0", 1), ("-", 1), ("=", 1), ("<--", 2)],

            [("Tab", 1.5), ("q", 1), ("w", 1), ("e", 1), ("r", 1), ("t", 1), ("y", 1),
             ("u", 1), ("i", 1), ("o", 1), ("p", 1), ("[", 1), ("]", 1), ("\\", 1.5)],

            [("CAPS", 1.8), ("a", 1), ("s", 1), ("d", 1), ("f", 1), ("g", 1),
             ("h", 1), ("j", 1), ("k", 1), ("l", 1), (";", 1), ("'", 1), ("ENTER", 2.35)],

            [("SHIFT", 2.30), ("z", 1), ("x", 1), ("c", 1), ("v", 1), ("b", 1),
             ("n", 1), ("m", 1), (",", 1), (".", 1), ("/", 1), ("Shift", 3.0)],

            [("CTRL", 1.25), ("Win", 1.25), ("ALT", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__rus_layout_uppercase = [
            [("ё", 1), ("!", 1), ('"', 1), ("№", 1), (";", 1), ("%", 1), (":", 1),
             ("?", 1), ("*", 1), ("(", 1), (")", 1), ("_", 1), ("+", 1), ("<--", 2)],

            [("Tab", 1.5), ("й", 1), ("ц", 1), ("у", 1), ("к", 1), ("е", 1), ("н", 1),
             ("г", 1), ("ш", 1), ("щ", 1), ("з", 1), ("х", 1), ("ъ", 1), ("\\", 1.5)],

            [("CAPS", 1.8), ("ф", 1), ("ы", 1), ("в", 1), ("а", 1), ("п", 1),
             ("р", 1), ("о", 1), ("л", 1), ("д", 1), ("ж", 1), ("э", 1), ("ENTER", 2.35)],

            [("SHIFT", 2.30), ("я", 1), ("ч", 1), ("с", 1), ("м", 1), ("и", 1),
             ("т", 1), ("ь", 1), ("б", 1), ("ю", 1), (".", 1), ("Shift", 3.0)],

            [("CTRL", 1.25), ("Win", 1.25), ("ALT", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__rus_layout_lowercase = [
            [("ё", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
             ("7", 1), ("8", 1), ("9", 1), ("0", 1), ("-", 1), ("=", 1), ("<--", 2)],

            [("Tab", 1.5), ("й", 1), ("ц", 1), ("у", 1), ("к", 1), ("е", 1), ("н", 1),
             ("г", 1), ("ш", 1), ("щ", 1), ("з", 1), ("х", 1), ("ъ", 1), ("\\", 1.5)],

            [("CAPS", 1.8), ("ф", 1), ("ы", 1), ("в", 1), ("а", 1), ("п", 1),
             ("р", 1), ("о", 1), ("л", 1), ("д", 1), ("ж", 1), ("э", 1), ("ENTER", 2.35)],

            [("SHIFT", 2.30), ("я", 1), ("ч", 1), ("с", 1), ("м", 1), ("и", 1),
             ("т", 1), ("ь", 1), ("б", 1), ("ю", 1), (".", 1), ("Shift", 3.0)],

            [("CTRL", 1.25), ("Win", 1.25), ("ALT", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        # self.__set_scale(1.0)

    def __create_keys(self):

        y_offset = self.__y

        if self.__language == KeyboardLanguage.ENGLISH:
            self.__create_keys_from_layout(
                y_offset,
                self.__eng_layout_uppercase if self.__is_upper_case else self.__eng_layout_lowercase
            )
        elif self.__language == KeyboardLanguage.RUSSIAN:
            self.__create_keys_from_layout(
                y_offset,
                self.__rus_layout_uppercase if self.__is_upper_case else self.__rus_layout_lowercase
            )

    def _switch_layout(self, keys: ScancodeWrapper):
        # Detect if shift has been pressed or released
        shift_pressed = keys[pygame.K_LSHIFT]

        # Only change case if the state is different
        if shift_pressed and not self.__is_upper_case:
            self.__is_upper_case = True
            self.__create_keys()  # Recreate keys with uppercase layout
            print('upper')

        elif not shift_pressed and self.__is_upper_case:
            self.__is_upper_case = False
            self.__create_keys()  # Recreate keys with lowercase layout
            print('lower')
        # print('.....')

    def __create_keys_from_layout(self, y_offset, layout):
        print('call __create_keys_from_layout')
        self.__keys = {}
        for row in layout:
            x_offset = self.__x
            for key, width in row:
                self.__keys[key] = pygame.Rect(x_offset, y_offset, self.__key_size * width, self.__key_size)
                x_offset += self.__key_size * width + self.__spacing
            y_offset += self.__key_size + self.__spacing

    def update(self, screen_height: int, screen_width: int, keys: ScancodeWrapper):
        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width
            scale_w = (screen_width * Keyboard.SIZE / Keyboard.LINE_KEYS_COUNT) / \
                (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
            self.__set_scale(scale_w)
        self._switch_layout(keys)

    def __set_scale(self, scale: float):
        self.__scale = scale
        self.__x = self.__screen_width / 2 - (Keyboard.LINE_KEYS_COUNT / 2.0 + 1) * Keyboard.KEY_SIZE * self.__scale
        self.__y = self.__screen_height / 2.5 + Keyboard.KEY_SIZE * self.__scale
        self.__key_size = Keyboard.KEY_SIZE * scale
        self.__spacing = Keyboard.KEY_SPACING * scale
        self.__font = pygame.font.Font(None, int(Keyboard.FONT_SIZE * scale))
        self.__create_keys()

    def highlight_key(self, key: str):
        if key in self.__keys:
            self.__highlighted_key = key
        elif key.upper() in self.__keys:
            self.__highlighted_key = key.upper()
        elif key.lower() in self.__keys:
            self.__highlighted_key = key.lower()
        if key == " ":
            self.__highlighted_key = "Space"

    def draw(self, screen: pygame.Surface):
        is_capslock = is_capslock_on()
        is_shift = is_shift_pressed()

        is_upper = is_capslock ^ is_shift

        for key, rect in self.__keys.items():
            bg_color = (30, 30, 30) if key != self.__highlighted_key else (35, 56, 35)
            pygame.draw.rect(screen, bg_color, rect, border_radius=5)

            if is_upper and len(key) == 1 and key.isalpha():
                key_str = key.upper()
            else:
                key_str = key

            text = self.__font.render(key_str, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
