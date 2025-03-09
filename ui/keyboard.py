
import pygame


class Keyboard:
    def __init__(self, x: int, y: int, key_size: int = 40):

        self.x = x
        self.y = y
        self.key_size = key_size
        self.spacing = 6
        self.keys = {}
        self.highlighted_key = None
        self.font = pygame.font.Font(None, 24)

        self.layout = [
            [("Esc", 1), ("1", 1), ("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1),
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

        self.create_keys()

    def create_keys(self):
        y_offset = self.y
        for row in self.layout:
            x_offset = self.x
            for key, width in row:
                self.keys[key] = pygame.Rect(x_offset, y_offset, self.key_size * width, self.key_size)
                x_offset += self.key_size * width + self.spacing
            y_offset += self.key_size + self.spacing

    def highlight_key(self, key):
        if key in self.keys:
            self.highlighted_key = key

    def draw(self, screen: pygame.Surface):
        for key, rect in self.keys.items():
            bg_color = (30, 30, 30) if key != self.highlighted_key else (255, 0, 0)
            pygame.draw.rect(screen, bg_color, rect, border_radius=5)
            text = self.font.render(key, True, (200, 200, 200))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
