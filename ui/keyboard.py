
import pygame


class Keyboard:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__keys = {}
        self.__highlighted_key = None
        self.__screen_height = -1
        self.__screen_width = -1

        self.__layout = [
            [("~", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
             ("7", 1), ("8", 1), ("9", 1), ("0", 1), ("-", 1), ("=", 1), ("<--", 2)],

            [("Tab", 1.5), ("Q", 1), ("W", 1), ("E", 1), ("R", 1), ("T", 1), ("Y", 1),
             ("U", 1), ("I", 1), ("O", 1), ("P", 1), ("[", 1), ("]", 1), ("\\", 1.5)],

            [("CapsLock", 1.8), ("A", 1), ("S", 1), ("D", 1), ("F", 1), ("G", 1),
             ("H", 1), ("J", 1), ("K", 1), ("L", 1), (";", 1), ("'", 1), ("Enter", 2.35)],

            [("LShift", 2.30), ("Z", 1), ("X", 1), ("C", 1), ("V", 1), ("B", 1),
             ("N", 1), ("M", 1), (",", 1), (".", 1), ("/", 1), ("RShift", 3.0)],

            [("LCtrl", 1.25), ("Win", 1.25), ("LAlt", 1.25), ("Space", 7.15),
             ("Alt", 1.25), ("Fn", 1.25), ("Menu", 1.25), ("RCtrl", 1.25)]
        ]
        # self.__set_scale(1.0)

    def __create_keys(self):
        y_offset = self.__y
        for row in self.__layout:
            x_offset = self.__x
            for key, width in row:
                self.__keys[key] = pygame.Rect(x_offset, y_offset, self.__key_size * width, self.__key_size)
                x_offset += self.__key_size * width + self.__spacing
            y_offset += self.__key_size + self.__spacing

    def update(self, screen_height: int, screen_width: int):
        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width
            scale_w = (screen_width * 0.6 / 15.0) / 40.0
            self.__set_scale(scale_w)

    def __set_scale(self, scale: float):
        self.__scale = scale
        self.__x = self.__screen_width / 2 - 8.5 * 40 * self.__scale
        self.__y = self.__screen_height / 2 + 1.0 * 40 * self.__scale
        self.__key_size = 40 * scale
        self.__spacing = 6 * scale
        self.__font = pygame.font.Font(None, int(24 * scale))
        self.__create_keys()

    def highlight_key(self, key: str):
        if key.upper() in self.__keys:
            self.__highlighted_key = key.upper()

    def draw(self, screen: pygame.Surface):
        for key, rect in self.__keys.items():
            bg_color = (30, 30, 30) if key != self.__highlighted_key else (35, 56, 35)
            pygame.draw.rect(screen, bg_color, rect, border_radius=5)
            text = self.__font.render(key, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
