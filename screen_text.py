
import pygame

from pygame.event import Event
from pygame.font import Font


class ScreenText:

    def __init__(self, screen: pygame.Surface):

        self.__screen = screen

        self.__font_size = 100
        self.__font = Font("fonts/UbuntuMono-Regular.ttf", self.__font_size)

        self.__input_text = ""
        self.__text_color = (255, 255, 255)

        self.__text_line_color = (0, 0, 0)

    def update(self, events: list[Event]):

        self.__text = self.__font.render(self.__input_text, True, self.__text_color)

        self.__text_line_rect = pygame.Rect(
            0, self.__screen.get_height() // 2,
            self.__screen.get_width(), self.__font_size
        )

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            if event.key == pygame.K_BACKSPACE:
                self.__input_text = self.__input_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.__input_text = ""
            else:
                if self.__text.get_width() < self.__text_line_rect.width:
                    self.__input_text += event.unicode

    def draw(self):
        pygame.draw.rect(self.__screen, self.__text_line_color, self.__text_line_rect)

        text_rect = pygame.Rect(self.__text_line_rect.x, self.__text_line_rect.y,
                                self.__text.get_width(), self.__text.get_height())

        self.__screen.blit(self.__text, text_rect)
