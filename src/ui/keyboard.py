import pygame
from pygame.key import ScancodeWrapper
from common.common import is_capslock_on, is_shift_pressed
from generators.keyboard_lang import KeyboardLanguage
from ui.fingers_enum import FingersEnum
import string


class Keyboard:

    KEY_SIZE = 40.0
    KEY_SPACING = 6.0
    FONT_SIZE = 24.0
    LINE_KEYS_COUNT = 15
    LINES_COUNT = 5
    WIDTH_SCALE = 0.7  # 70% of the screen
    HEIGHT_SCALE = 0.45  # 45% of the screen

    POINTER_RED = (230, 10, 10)
    RED = (180, 100, 102)
    YELLOW = (190, 190, 100)
    GREEN = (100, 180, 105)
    BLUE = (110, 190, 190)
    PINK = (190, 130, 185)
    PURPLE = (130, 125, 190)
    GREY = (115, 115, 115)

    REGULAR_BG_KEY_COLOR = (30, 30, 30)

    def __init__(self, language: KeyboardLanguage, relative_y_pos: float):
        self.__relative_y_pos = relative_y_pos
        self.__keys = []
        self.__highlighted_key = None
        self.__language = language
        self.__is_upper_case = False

        self.__finger: FingersEnum | None = None
        self.__finger_is_visible = False

        self.__key_size = Keyboard.KEY_SIZE
        self.__spacing = Keyboard.KEY_SPACING

        self.__negative_layout = []

        self.__color_layout = [
            self.RED, self.RED, self.RED, self.YELLOW, self.GREEN, self.BLUE, self.BLUE,
            self.PINK, self.PINK, self.RED, self.YELLOW, self.GREEN, self.GREEN, self.GREEN,  # First row

            self.RED, self.RED, self.YELLOW, self.GREEN, self.BLUE, self.BLUE, self.PINK,
            self.PINK, self.RED, self.YELLOW, self.GREEN, self.GREEN, self.GREEN, self.GREEN,  # Second row

            self.RED, self.RED, self.YELLOW, self.GREEN, self.BLUE, self.BLUE, self.PINK,
            self.PINK, self.RED, self.YELLOW, self.GREEN, self.GREEN, self.GREEN,  # Third row

            self.RED, self.RED, self.YELLOW, self.GREEN, self.BLUE, self.BLUE,
            self.PINK, self.PINK, self.RED, self.YELLOW, self.GREEN, self.GREEN,  # Fourth row

            self.GREY, self.GREY, self.GREY, self.PURPLE, self.GREY, self.GREY, self.GREY, self.GREY  # Space bar row
        ]

        self.__fingers_layout = [
            FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_RING, FingersEnum.LEFT_MIDDLE, FingersEnum.LEFT_INDEX, FingersEnum.LEFT_INDEX,
            FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_MIDDLE, FingersEnum.RIGHT_RING, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE,  # First row

            FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_RING, FingersEnum.LEFT_MIDDLE, FingersEnum.LEFT_INDEX, FingersEnum.LEFT_INDEX, FingersEnum.RIGHT_INDEX,
            FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_MIDDLE, FingersEnum.RIGHT_RING, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE,  # Second row

            FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_RING, FingersEnum.LEFT_MIDDLE, FingersEnum.LEFT_INDEX, FingersEnum.LEFT_INDEX, FingersEnum.RIGHT_INDEX,
            FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_MIDDLE, FingersEnum.RIGHT_RING, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE,  # Third row

            FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_LITTLE, FingersEnum.LEFT_RING, FingersEnum.LEFT_MIDDLE, FingersEnum.LEFT_INDEX, FingersEnum.LEFT_INDEX,
            FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_INDEX, FingersEnum.RIGHT_MIDDLE, FingersEnum.RIGHT_RING, FingersEnum.RIGHT_LITTLE, FingersEnum.RIGHT_LITTLE,  # Fourth row

            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.BOTH_THUMBS, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE  # Space bar row
        ]

        self.__pointer_fingers_layout = [
            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,
            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,  # First row

            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,
            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,  # Second row

            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.BOTH_INDEXES, FingersEnum.NONE, FingersEnum.NONE,
            FingersEnum.BOTH_INDEXES, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,  # Third row

            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,
            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE,  # Fourth row

            FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE, FingersEnum.NONE  # Space bar row
        ]

        self.__eng_layout_uppercase = [
            [("~", 1), ("!", 1), ("@", 1), ("#", 1), ("$", 1), ("%", 1), ("^", 1),
             ("&", 1), ("*", 1), ("(", 1), (")", 1), ("_", 1), ("+", 1), ("<--", 2)],

            [("Tab", 1.5), ("q", 1), ("w", 1), ("e", 1), ("r", 1), ("t", 1), ("y", 1),
             ("u", 1), ("i", 1), ("o", 1), ("p", 1), ("{", 1), ("}", 1), ("|", 1.5)],

            [("Caps", 1.8), ("a", 1), ("s", 1), ("d", 1), ("f", 1), ("g", 1),
             ("h", 1), ("j", 1), ("k", 1), ("l", 1), (":", 1), ('"', 1), ("Enter", 2.35)],

            [("L-Shift", 2.30), ("z", 1), ("x", 1), ("c", 1), ("v", 1), ("b", 1),
             ("n", 1), ("m", 1), ("<", 1), (">", 1), ("?", 1), ("R-Shift", 3.0)],

            [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__eng_layout_lowercase = [
            [("`", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
             ("7", 1), ("8", 1), ("9", 1), ("0", 1), ("-", 1), ("=", 1), ("<--", 2)],

            [("Tab", 1.5), ("q", 1), ("w", 1), ("e", 1), ("r", 1), ("t", 1), ("y", 1),
             ("u", 1), ("i", 1), ("o", 1), ("p", 1), ("[", 1), ("]", 1), ("\\", 1.5)],

            [("Caps", 1.8), ("a", 1), ("s", 1), ("d", 1), ("f", 1), ("g", 1),
             ("h", 1), ("j", 1), ("k", 1), ("l", 1), (";", 1), ("'", 1), ("Enter", 2.35)],

            [("L-Shift", 2.30), ("z", 1), ("x", 1), ("c", 1), ("v", 1), ("b", 1),
             ("n", 1), ("m", 1), (",", 1), (".", 1), ("/", 1), ("R-Shift", 3.0)],

            [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__rus_layout_uppercase = [
            [("ё", 1), ("!", 1), ('"', 1), ("Nº", 1), (";", 1), ("%", 1), (":", 1),
             ("?", 1), ("*", 1), ("(", 1), (")", 1), ("_", 1), ("+", 1), ("<--", 2)],

            [("Tab", 1.5), ("й", 1), ("ц", 1), ("у", 1), ("к", 1), ("е", 1), ("н", 1),
             ("г", 1), ("ш", 1), ("щ", 1), ("з", 1), ("х", 1), ("ъ", 1), ("/", 1.5)],

            [("Caps", 1.8), ("ф", 1), ("ы", 1), ("в", 1), ("а", 1), ("п", 1),
             ("р", 1), ("о", 1), ("л", 1), ("д", 1), ("ж", 1), ("э", 1), ("Enter", 2.35)],

            [("L-Shift", 2.30), ("я", 1), ("ч", 1), ("с", 1), ("м", 1), ("и", 1),
             ("т", 1), ("ь", 1), ("б", 1), ("ю", 1), (",", 1), ("R-Shift", 3.0)],

            [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__rus_layout_lowercase = [
            [("ё", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
             ("7", 1), ("8", 1), ("9", 1), ("0", 1), ("-", 1), ("=", 1), ("<--", 2)],

            [("Tab", 1.5), ("й", 1), ("ц", 1), ("у", 1), ("к", 1), ("е", 1), ("н", 1),
             ("г", 1), ("ш", 1), ("щ", 1), ("з", 1), ("х", 1), ("ъ", 1), ("\\", 1.5)],

            [("Caps", 1.8), ("ф", 1), ("ы", 1), ("в", 1), ("а", 1), ("п", 1),
             ("р", 1), ("о", 1), ("л", 1), ("д", 1), ("ж", 1), ("э", 1), ("Enter", 2.35)],

            [("L-Shift", 2.30), ("я", 1), ("ч", 1), ("с", 1), ("м", 1), ("и", 1),
             ("т", 1), ("ь", 1), ("б", 1), ("ю", 1), (".", 1), ("R-Shift", 3.0)],

            [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)]
        ]

        self.__create_keys()

    def __create_keys(self):
        if self.__language == KeyboardLanguage.ENGLISH:
            layout = self.__eng_layout_uppercase if self.__is_upper_case else self.__eng_layout_lowercase
            self.__negative_layout = self.__eng_layout_lowercase if self.__is_upper_case else self.__eng_layout_uppercase
        elif self.__language == KeyboardLanguage.RUSSIAN:
            layout = self.__rus_layout_uppercase if self.__is_upper_case else self.__rus_layout_lowercase
            self.__negative_layout = self.__rus_layout_lowercase if self.__is_upper_case else self.__rus_layout_uppercase
        self.__create_keys_from_layout(layout)

    def _switch_layout(self, keys: ScancodeWrapper):
        # Detect if shift has been pressed or released
        shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        # Only change case if the state is different
        if shift_pressed and not self.__is_upper_case:
            self.__is_upper_case = True
            self.__create_keys()  # Recreate keys with uppercase layout
            print('upper')

        elif not shift_pressed and self.__is_upper_case:
            self.__is_upper_case = False
            self.__create_keys()  # Recreate keys with lowercase layout
            print('lower')

    def __create_keys_from_layout(self, layout):
        print('call __create_keys_from_layout')
        self.__keys = []
        y_offset = 0
        for row in layout:
            x_offset = 0
            for key, width in row:
                rect = pygame.Rect(x_offset, y_offset, self.__key_size * width, self.__key_size)
                self.__keys.append((key, rect))
                x_offset += self.__key_size * width + self.__spacing
            y_offset += self.__key_size + self.__spacing

    def update(self, keys: ScancodeWrapper):
        self._switch_layout(keys)

    def change_color(self, color, factor=0.5):
        r, g, b = color
        r = min(int(r * factor), 255)
        g = min(int(g * factor), 255)
        b = min(int(b * factor), 255)
        return (r, g, b)

    def __shift_test(self, key: str):
        for row in self.__negative_layout:
            for (neg_key, rect) in row:
                if self.__negative_layout.index(row) == 0 or 2 <= self.__negative_layout.index(row) <= 3:
                    cut_end = len(row) // 2 - 1
                elif self.__negative_layout.index(row) == 1:
                    cut_end = len(row) // 2 - 2

                if row.index((neg_key, rect)) <= cut_end:
                    if neg_key.lower() == key.lower():
                        self.__highlighted_key = "R-Shift"
                        return
                else:
                    if neg_key.lower() == key.lower():
                        self.__highlighted_key = "L-Shift"
                        return

    def highlight_key(self, key: str, next_word_slice: str) -> None:
        keys_only = [k for k, _ in self.__keys]

        if key == " ":
            self.__highlighted_key = "Space"
            return

        is_shift = is_shift_pressed()
        is_caps = is_capslock_on()

        if key in keys_only:
            for row in self.__negative_layout:
                for (neg_key, _) in row:
                    if neg_key == key:
                        if is_caps:
                            self.__highlighted_key = "Caps"
                            return
                        elif is_shift:
                            self.__highlighted_key = None
                            return

            self.__highlighted_key = key
            return

        if key in string.punctuation:
            self.__shift_test(key)
            return

        if is_shift or is_caps:
            for row in self.__negative_layout:
                for (neg_key, _) in row:
                    if neg_key.lower() == key.lower():
                        self.__highlighted_key = neg_key
                        return

            if key in keys_only:
                self.__highlighted_key = key
                return

        if not is_shift and not is_caps:
            if all(letter.isupper() or letter in string.punctuation for letter in next_word_slice) \
                    and key not in string.punctuation:
                self.__highlighted_key = "Caps"
                return

            self.__shift_test(key)

    def highlight_finger_key(self, finger: FingersEnum, is_visible: bool):
        self.__finger = finger
        self.__finger_is_visible = is_visible

    def draw(self, screen: pygame.Surface):

        scale_w = (screen.width * Keyboard.WIDTH_SCALE / Keyboard.LINE_KEYS_COUNT) / \
            (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
        scale_h = (screen.height * Keyboard.HEIGHT_SCALE / Keyboard.LINES_COUNT) / \
            (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
        scale = min(scale_w, scale_h)

        y = screen.height * self.__relative_y_pos + self.__key_size
        x = screen.width / 2 - (Keyboard.LINE_KEYS_COUNT / 2.0 + 1) * self.__key_size * scale

        self.__font = pygame.font.Font(None, int(Keyboard.FONT_SIZE * scale))

        is_capslock = is_capslock_on()
        is_shift = is_shift_pressed()

        is_upper = is_capslock ^ is_shift

        layout_zip = zip(self.__keys, self.__color_layout, self.__fingers_layout, self.__pointer_fingers_layout)
        for (key, raw_rect), color, finger, pointer_finger in layout_zip:
            rect = pygame.rect.Rect(
                raw_rect.x * scale + x,
                raw_rect.y * scale + y,
                raw_rect.width * scale,
                raw_rect.height * scale
            )

            bg_color = self.REGULAR_BG_KEY_COLOR

            if key == self.__highlighted_key or (self.__finger == finger and self.__finger_is_visible):
                bg_color = self.change_color(color)
            elif self.__finger == pointer_finger and self.__finger_is_visible:
                bg_color = self.change_color(self.POINTER_RED)

            pygame.draw.rect(screen, bg_color, rect, border_radius=5)
            pygame.draw.rect(screen, color, rect, int(1.5 * scale))

            if is_upper and len(key) == 1 and key.isalpha():
                key_str = key.upper()
            else:
                key_str = key

            text = self.__font.render(key_str, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

    def set_language(self, language: KeyboardLanguage):
        self.__language = language
        self.__create_keys()
