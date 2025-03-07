
import pygame

from pygame.event import Event
from pygame.font import Font


class ScreenText:

    def __init__(self, screen: pygame.Surface):

        self.__screen = screen

        self.__font_size = 100
        self.__font = Font(None, self.__font_size)

        self.__input_text = ""
        self.__text = self.__font.render(self.__input_text, True, (255, 255, 255))
        self.__text_color = (255, 255, 255)

        self.__text_line_color = (0, 0, 0)
        self.__text_line_rect = pygame.Rect(0, self.__screen.get_height()//2,
                                            self.__screen.get_width(), self.__text.get_height()+10)

        self.__text_rect = pygame.Rect(self.__text_line_rect.x, self.__text_line_rect.y,
                                       self.__text.get_width(), self.__text.get_height())

    def update(self, events: list[Event], keys):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    print(event.key)
                    if event.key == pygame.K_BACKSPACE:  # Удаление символа
                        self.__input_text = self.__input_text[:-1]
                    elif event.key == pygame.K_RETURN:  # Если нажата клавиша Enter
                        self.__input_text = ""
                    elif self.__text.get_width() < self.__screen.get_width()-20:  # Если длина текста меньше максимальной
                        self.__input_text += event.unicode

        self.__text = self.__font.render(self.__input_text, True, self.__text_color)

        self.__text_rect = pygame.Rect(self.__text_line_rect.x, self.__text_line_rect.y,
                                       self.__text.get_width(), self.__text.get_height())

    def draw(self):
        pygame.draw.rect(self.__screen, self.__text_line_color, self.__text_line_rect)

        self.__screen.blit(self.__text, self.__text_rect)
