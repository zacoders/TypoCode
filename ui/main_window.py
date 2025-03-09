import pygame
from pygame.event import Event
from ui.font_calc import FontCalc
from ui.input_line import InputLine
from ui.random_line import RandomLine


class MainWindow:

    def __init__(self):
        self.__text_len = 34
        self.__random_line = RandomLine(self.__text_len)
        self.__input_line = InputLine(self.__random_line)
        self.__font_calc = FontCalc()

    def update(self, events: list[Event], screen_width):
        
        self.__font_calc.update(self.__text_len, screen_width)
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            self.__input_line.update(event)

    def draw(self, screen: pygame.Surface):
        self.__input_line.draw(screen, self.__font_calc.current_font_size())
        self.__random_line.draw(screen, self.__font_calc.current_font_size())
