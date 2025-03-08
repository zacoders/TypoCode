
from pygame.font import Font
from pygame.event import Event
import pygame


class InputLine:

    def __init__(self):
        self.__text = ''
        self.__font_size = 100
        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)
        self.__font = Font("fonts/Inconsolata-Regular.ttf", self.__font_size)

    def update(self, event: Event):
        if event.key == pygame.K_BACKSPACE:
            self.__text = self.__text[:-1]
        elif event.key == pygame.K_RETURN:
            self.__text = ""
        else:
            self.__text += event.unicode

    def draw(self, screen: pygame.Surface):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 2,
            screen.get_width(),
            self.__font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)
        text = self.__font.render(self.__text, True, self.__text_color)
        screen.blit(text, line_rect)
