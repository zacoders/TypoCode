
import pygame
from pygame.key import ScancodeWrapper
from common.common import is_capslock_on, is_shift_pressed
from generators.keyboard_lang import KeyboardLanguage
from ui.fingers_enum import FingersEnum


class Keyboard:

    KEY_SIZE = 40.0
    KEY_SPACING = 6.0
    FONT_SIZE = 24.0
    LINE_KEYS_COUNT = 15
    LINES_COUNT = 5
    WIDTH_SCALE = 0.7  # 70% of the screen
    HEIGHT_SCALE = 0.45  # 45% of the screen

    RED = (180, 100, 102)
    YELLOW = (190, 190, 100)
    GREEN = (100, 180, 105)
    BLUE = (110, 190, 190)
    PINK = (190, 130, 185)
    PURPLE = (130, 125, 190)
    GREY = (115, 115, 115)

    REGULAR_BG_KEY_COLOR = (30, 30, 30)

    def __init__(self, language: KeyboardLanguage, relative_y_pos: float = 0):
        self.__relative_y_pos = relative_y_pos
        self.__x = 0
        self.__y = 0
        self.__keys = []
        self.__highlighted_key = None
        self.__screen_height = -1
        self.__screen_width = -1
        self.__language = language
        self.__is_upper_case = False
        self.__highlighted_finger_keys = []
        self.__start_button_keys = []

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

    def __create_keys_from_layout(self, y_offset, layout):
        print('call __create_keys_from_layout')
        self.__keys = []
        for row in layout:
            x_offset = self.__x
            for key, width in row:
                rect = pygame.Rect(x_offset, y_offset, self.__key_size * width, self.__key_size)
                self.__keys.append((key, rect))
                x_offset += self.__key_size * width + self.__spacing
            y_offset += self.__key_size + self.__spacing

    def update(self, screen_height: int, screen_width: int, keys: ScancodeWrapper):
        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width
            scale_w = (screen_width * Keyboard.WIDTH_SCALE / Keyboard.LINE_KEYS_COUNT) / \
                (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
            scale_h = (screen_height * Keyboard.HEIGHT_SCALE / Keyboard.LINES_COUNT) / \
                (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
            self.__set_scale(min(scale_w, scale_h))
        self._switch_layout(keys)

    def __set_scale(self, scale: float):
        self.__scale = scale
        self.__x = self.__screen_width / 2 - (Keyboard.LINE_KEYS_COUNT / 2.0 + 1) * Keyboard.KEY_SIZE * self.__scale
        self.__y = self.__screen_height * self.__relative_y_pos + Keyboard.KEY_SIZE * self.__scale
        self.__key_size = Keyboard.KEY_SIZE * scale
        self.__spacing = Keyboard.KEY_SPACING * scale
        self.__font = pygame.font.Font(None, int(Keyboard.FONT_SIZE * scale))
        self.__create_keys()

    def change_color(self, color, factor=0.5):
        r, g, b = color
        r = min(int(r * factor), 255)
        g = min(int(g * factor), 255)
        b = min(int(b * factor), 255)
        return (r, g, b)

    def highlight_key(self, key: str):
        keys_only = [k for k, _ in self.__keys]
        if key in keys_only:
            self.__highlighted_key = key
        elif key.upper() in keys_only:
            self.__highlighted_key = key.upper()
        elif key.lower() in keys_only:
            self.__highlighted_key = key.lower()
        if key == " ":
            self.__highlighted_key = "Space"

    def highlight_fingers_key(self, finger_enum: FingersEnum, is_visible: bool):
        self.__highlighted_finger_keys = []
        self.__start_button_keys = []

        def filter_keys_by_color(target_color, finger_enum: FingersEnum):
            finger_side = finger_enum.name.split('_')[0]  # "LEFT" или "RIGHT"
            filtered_keys = []

            keys_only = [k for k, _ in self.__keys]

            row_lengths = [14, 14, 13, 12, 8]
            start_index = 0

            for row_len in row_lengths:
                end_index = start_index + row_len

                row_colors = self.__color_layout[start_index:end_index]
                row_keys = keys_only[start_index:end_index]

                middle = row_len // 2

                if finger_side == "LEFT":
                    zone_colors = row_colors[:middle]
                    zone_keys = row_keys[:middle]
                elif finger_side == "RIGHT":
                    zone_colors = row_colors[-middle - 1:]
                    zone_keys = row_keys[-middle - 1:]
                else:
                    zone_colors = row_colors
                    zone_keys = row_keys

                for key, color in zip(zone_keys, zone_colors):
                    if is_visible:
                        if color == target_color:
                            filtered_keys.append(key)

                start_index = end_index  # Переход к следующей строке

            return filtered_keys

        keys_only = [k for k, _ in self.__keys]

        finger_color_map = {
            FingersEnum.BOTH_THUMBS: self.PURPLE,
            FingersEnum.LEFT_INDEX: self.BLUE,
            FingersEnum.RIGHT_INDEX: self.PINK,
            FingersEnum.LEFT_MIDDLE: self.GREEN,
            FingersEnum.RIGHT_LITTLE: self.GREEN,
            FingersEnum.LEFT_RING: self.YELLOW,
            FingersEnum.RIGHT_RING: self.YELLOW,
            FingersEnum.LEFT_LITTLE: self.RED,
            FingersEnum.RIGHT_MIDDLE: self.RED
        }

        for enum, color in finger_color_map.items():
            if finger_enum == enum:
                self.__highlighted_finger_keys = filter_keys_by_color(color, finger_enum)
                return

        if finger_enum == FingersEnum.BOTH_INDEXES:
            if self.__language == KeyboardLanguage.ENGLISH:
                keys = [k for k in keys_only if k in ("f", "F", "j", "J")]
            elif self.__language == KeyboardLanguage.RUSSIAN:
                keys = [k for k in keys_only if k in ("а", "А", "о", "О")]

            self.__highlighted_finger_keys = keys if is_visible else []
            self.__start_button_keys = keys if is_visible else []

    def draw(self, screen: pygame.Surface):
        is_capslock = is_capslock_on()
        is_shift = is_shift_pressed()

        is_upper = is_capslock ^ is_shift

        for (key, rect), color in zip(self.__keys, self.__color_layout):
            if key not in self.__highlighted_finger_keys:
                bg_color = self.REGULAR_BG_KEY_COLOR if key != self.__highlighted_key else self.change_color(color)
            else:
                if key in self.__start_button_keys:
                    bg_color = self.change_color((180, 70, 70))
                else:
                    bg_color = self.change_color(color)

            pygame.draw.rect(screen, bg_color, rect, border_radius=5)
            pygame.draw.rect(screen, color, rect, int(1.5 * self.__scale))

            if is_upper and len(key) == 1 and key.isalpha():
                key_str = key.upper()
            else:
                key_str = key

            text = self.__font.render(key_str, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
