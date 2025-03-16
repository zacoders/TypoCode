
from pygame.font import Font
import pygame

from typing_errors import TypingErrors
from generators.generator_abc import GeneratorABC


class RandomLine:

    def __init__(self, text_len: int, errors: TypingErrors, text_generator: GeneratorABC, font_file_path: str):

        self.__text_len = text_len

        self.__errors = errors

        self.__text_generator = text_generator
        self.__text = self.__text_generator.get_text(self.__text_len, self.__errors)
        self.__text_color = (155, 255, 155)
        self.__text_line_color = (0, 0, 0)

        self.__prev_font_size = 100
        self.__font_file_path = font_file_path
        self.__font = Font(font_file_path, self.__prev_font_size)

    @property
    def text_len(self):
        return self.__text_len

    def update(self):
        ...

    def draw(self, screen: pygame.Surface, font_size: int, text_width: int):
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
        diff_x = (screen.get_width() - text_width) / 2
        text_pos = (diff_x, line_rect.y)
        screen.blit(text, text_pos)

    def get_text(self) -> str:
        return self.__text

    def next_line(self):
        self.__text = self.__text_generator.get_text(self.__text_len, self.__errors)

    def set_errors(self, errors: TypingErrors):
        self.__errors = errors
