
from pygame.font import Font
from pygame.event import Event
import pygame

from errors import Errors
from generators.base import BaseGenerator


class RandomLine:

    def __init__(self, text_len: int, errors: Errors, text_generator: BaseGenerator, font_file_path: str):

        self.__text_len = text_len

        self.__errors = errors

        self.__text_generator = text_generator
        self.__text = self.__text_generator.get_text(self.__text_len, self.__errors)

        self.__text_color = (155, 255, 155)
        self.__text_line_color = (0, 0, 0)

        self.__prev_font_size = 100
        self.__font_file_path = font_file_path
        self.__font = Font(font_file_path, self.__prev_font_size)

    def update(self):
        ...

    def draw(self, screen: pygame.Surface, font_size: int):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 3 - font_size,
            screen.get_width(),
            font_size
        )

        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        if self.__prev_font_size != font_size:
            self.__font = Font(self.__font_file_path, font_size)
            self.__prev_font_size = font_size

        text = self.__font.render(self.__text, True, self.__text_color)

        char_width = self.__font.render("a", False, (255, 255, 255)).get_width()
        screen.blit(text, (line_rect.x + char_width, line_rect.y))

    def get_text(self) -> str:
        return self.__text

    def next_line(self):
        self.__text = self.__text_generator.get_text(self.__text_len, self.__errors)

    def set_errors(self, errors: Errors):
        self.__errors = errors
