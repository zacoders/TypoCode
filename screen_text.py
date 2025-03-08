
import random
import string
import pygame

from pygame.event import Event
from pygame.font import Font


class ScreenText:

    def __init__(self, screen: pygame.Surface):

        self.__screen = screen

        self.__font_size = 100
        self.__font = Font("fonts/UbuntuMono-Regular.ttf", self.__font_size)

        self.__max_symbols_count = 27

        self.__input_print_text = ""
        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)

        self.__input_rand_text = ""
        self.__rand_text_color = (255, 255, 255)
        self.__rand_text_line_color = (0, 0, 0)

    def update(self, events: list[Event]):

        self.__print_line_rect = pygame.Rect(
            0, self.__screen.get_height() // 2,
            self.__screen.get_width(), self.__font_size)

        self.__rand_text_line_rect = pygame.Rect(
            self.__print_line_rect.x, self.__print_line_rect.y - self.__print_line_rect.height,
            self.__screen.get_width(), self.__font_size)

        for symbol in range(self.__max_symbols_count):
            random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
            if len(self.__input_rand_text) < self.__max_symbols_count:
                self.__input_rand_text += random_char

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            if event.key == pygame.K_BACKSPACE:
                self.__input_print_text = self.__input_print_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.__input_print_text = ""
            else:
                if len(self.__input_print_text) < self.__max_symbols_count:
                    self.__input_print_text += event.unicode

    def draw(self):
        pygame.draw.rect(self.__screen, self.__text_line_color, self.__print_line_rect)

        print_text = self.__font.render(self.__input_print_text, True, self.__text_color)

        print_text_rect = pygame.Rect(
            self.__print_line_rect.x,
            self.__print_line_rect.y,
            print_text.get_width(),
            print_text.get_height())

        self.__screen.blit(print_text, print_text_rect)

        pygame.draw.rect(self.__screen, self.__rand_text_line_color, self.__rand_text_line_rect)

        rand_text = self.__font.render(self.__input_rand_text, True, self.__rand_text_color)

        rand_text_rect = pygame.Rect(
            self.__rand_text_line_rect.x,
            self.__rand_text_line_rect.y,
            rand_text.get_width(),
            rand_text.get_height())

        self.__screen.blit(rand_text, rand_text_rect)
