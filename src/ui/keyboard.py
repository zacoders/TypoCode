from typing import Tuple
import pygame
from common.common import is_capslock_on, is_shift_pressed, uppercase_percentage
from generators.keyboard_lang import KeyboardLanguage
from ui.fingers_enum import FingersEnum
from ui.keyboard_layouts import KeyboardLayouts


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

    def __init__(self, language: KeyboardLanguage, relative_y_pos: float, is_upper_layout: bool = False):
        self.__relative_y_pos = relative_y_pos
        self.__highlighted_key = None
        self.__language = language
        self.__highlighted_finger: FingersEnum | None = None
        self.__highlight_finger_is_visible = False
        self.__is_upper_layout = is_upper_layout

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

        key_lengths = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5],
            [1.8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2.35],
            [2.30, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3.0],
            [1.25, 1.25, 1.25, 7.15, 1.25, 1.25, 1.25, 1.25]
        ]
        self.__key_sizes = self.__create_key_sizes(key_lengths)

    @classmethod
    def __create_key_sizes(cls, key_lengths):
        key_sizes = []
        y_offset = 0
        for width_row in key_lengths:
            x_offset = 0
            for width in width_row:
                rect = pygame.Rect(x_offset, y_offset, cls.KEY_SIZE * width, cls.KEY_SIZE)
                key_sizes.append(rect)
                x_offset += cls.KEY_SIZE * width + cls.KEY_SPACING
            y_offset += cls.KEY_SIZE + cls.KEY_SPACING
        return key_sizes

    def update(self):
        ...

    def change_color(self, color, factor=0.5):
        r, g, b = color
        r = min(int(r * factor), 255)
        g = min(int(g * factor), 255)
        b = min(int(b * factor), 255)
        return (r, g, b)

    def __is_left_finger(self, finger: FingersEnum) -> bool:
        return finger in {
            FingersEnum.LEFT_THUMB,
            FingersEnum.LEFT_INDEX,
            FingersEnum.LEFT_MIDDLE,
            FingersEnum.LEFT_RING,
            FingersEnum.LEFT_LITTLE,
        }

    def __get_finger_by_key(self, key: str):
        layout = KeyboardLayouts.get_layout(self.__language, False, False)

        if key in layout:
            return layout.index(key)

        caps_layout = KeyboardLayouts.get_layout(self.__language, False, True)

        if key in caps_layout:
            return caps_layout.index(key)

        shift_layout = KeyboardLayouts.get_layout(self.__language, True, False)

        if key in shift_layout:
            return shift_layout.index(key)

        raise Exception(f"Key '{key}' not found in any layout.")

    def highlight_key(self, key_to_press: str, prev_key: str, word: str):
        is_capslock = is_capslock_on()
        is_shift = is_shift_pressed()

        if len(word) > 2:
            if uppercase_percentage(word) >= 0.5 and not is_capslock:
                self.__highlighted_key = "Caps"
                return
            if uppercase_percentage(word) <= 0.5 and is_capslock:
                self.__highlighted_key = "Caps"
                return

        self.__highlighted_key = key_to_press

        layout = KeyboardLayouts.get_layout(self.__language, is_shift, is_capslock)

        if key_to_press in layout:
            return

        if key_to_press == " ":
            finger_index = self.__get_finger_by_key(prev_key)
            finger = self.__fingers_layout[finger_index]
            if self.__is_left_finger(finger):
                self.__highlighted_key = "R-Space"
            else:
                self.__highlighted_key = "L-Space"
            return

        if not is_shift:
            finger_index = self.__get_finger_by_key(key_to_press)
            finger = self.__fingers_layout[finger_index]
            if self.__is_left_finger(finger):
                self.__highlighted_key = "R-Shift"
            else:
                self.__highlighted_key = "L-Shift"
            return

    def highlight_fingers_key(self, finger: FingersEnum, is_visible: bool):
        self.__highlighted_finger = finger
        self.__highlight_finger_is_visible = is_visible

    def __draw_highlighted_space(
        self,
        screen: pygame.Surface,
        bg_color: Tuple[int, int, int],
        rect: pygame.Rect,
        is_left: bool
    ) -> None:
        if is_left:
            x = rect.x
        else:
            x = rect.x + rect.width // 2
        pygame.draw.rect(
            screen,
            bg_color,
            (x, rect.y, rect.width // 2, rect.height)
        )

    def draw(self, screen: pygame.Surface):
        scale_w = (screen.width * Keyboard.WIDTH_SCALE / Keyboard.LINE_KEYS_COUNT) / \
            (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
        scale_h = (screen.height * Keyboard.HEIGHT_SCALE / Keyboard.LINES_COUNT) / \
            (Keyboard.KEY_SIZE + Keyboard.KEY_SPACING)
        scale = min(scale_w, scale_h)
        y = screen.height * self.__relative_y_pos + self.KEY_SIZE
        x = screen.width / 2 - (Keyboard.LINE_KEYS_COUNT / 2.0 + 1) * self.KEY_SIZE * scale
        self.__font = pygame.font.Font(None, int(Keyboard.FONT_SIZE * scale))

        if self.__is_upper_layout:
            is_capslock = True
            is_shift = False
        else:
            is_capslock = is_capslock_on()
            is_shift = is_shift_pressed()

        is_upper = is_capslock ^ is_shift

        layout_zip = zip(
            KeyboardLayouts.get_layout(self.__language, is_shift, is_capslock),
            self.__key_sizes,
            self.__color_layout,
            self.__fingers_layout,
            self.__pointer_fingers_layout
        )

        for key, raw_rect, color, finger, pointer_finger in layout_zip:
            rect = pygame.rect.Rect(
                raw_rect.x * scale + x,
                raw_rect.y * scale + y,
                raw_rect.width * scale,
                raw_rect.height * scale
            )
            bg_color = self.REGULAR_BG_KEY_COLOR

            if key == self.__highlighted_key or (self.__highlighted_finger ==
                                                 finger and self.__highlight_finger_is_visible):
                bg_color = self.change_color(color)
                pygame.draw.rect(screen, bg_color, rect)

            elif key == "Space":
                pygame.draw.rect(screen, bg_color, rect)
                bg_color = self.change_color(color)

                if self.__highlighted_key == "L-Space":
                    self.__draw_highlighted_space(screen, bg_color, rect, is_left=True)
                elif self.__highlighted_key == "R-Space":
                    self.__draw_highlighted_space(screen, bg_color, rect, is_left=False)

                if self.__highlight_finger_is_visible:
                    if self.__highlighted_finger == FingersEnum.LEFT_THUMB:
                        self.__draw_highlighted_space(screen, bg_color, rect, is_left=True)
                    elif self.__highlighted_finger == FingersEnum.RIGHT_THUMB:
                        self.__draw_highlighted_space(screen, bg_color, rect, is_left=False)

            elif self.__highlighted_finger == pointer_finger and self.__highlight_finger_is_visible:
                bg_color = self.change_color(self.POINTER_RED)
                pygame.draw.rect(screen, bg_color, rect)

            else:
                pygame.draw.rect(screen, bg_color, rect)

            pygame.draw.rect(screen, color, rect, int(1.3 * scale))

            if is_upper and len(key) == 1 and key.isalpha():
                key_str = key.upper()
            else:
                key_str = key

            text = self.__font.render(key_str, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

    def set_language(self, language: KeyboardLanguage):
        self.__language = language
