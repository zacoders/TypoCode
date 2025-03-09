
from pygame.font import Font
from pygame.event import Event
import pygame

from generators.python import PythonGenerator


class RandomLine:

    def __init__(self, text_len: int):

        self.__text_len = text_len

        self.__text_generator = PythonGenerator()
        self.__text = self.__text_generator.get(self.__text_len)

        self.__text_color = (155, 255, 155)
        self.__text_line_color = (0, 0, 0)

        self.__prev_font_size = 100
        self.__font = Font("fonts/Inconsolata-Regular.ttf", self.__prev_font_size)

    def update(self, event: Event):
        if event.key == pygame.K_BACKSPACE:
            self.__text = self.__text[:-1]
        elif event.key == pygame.K_RETURN:
            self.__text = ""
        else:
            self.__input_text += event.unicode

    def draw(self, screen: pygame.Surface, font_size: int):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 2 - 100,
            screen.get_width(),
            font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        if self.__prev_font_size != font_size:
            if  5 < font_size < 1000:
                self.__font = Font("fonts/Inconsolata-Regular.ttf", font_size)
                self.__prev_font_size = font_size
            else:
                return

        text = self.__font.render(self.__text, True, self.__text_color)
        screen.blit(text, line_rect)

    def get_text(self) -> str:
        return self.__text

    def next_line(self):
        self.__text = self.__text_generator.get(self.__text_len)
