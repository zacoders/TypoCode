import pygame
from pygame.event import Event
from ui.font_calc import FontCalc
from ui.input_line import InputLine
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class MainWindow:

    def __init__(self):
        self.__text_len = 64
        self.__keyboard = Keyboard()
        self.__random_line = RandomLine(self.__text_len)
        self.__input_line = InputLine(self.__random_line, self.__keyboard)
        self.__font_calc = FontCalc()

    def update(self, events: list[Event], screen_height: int, screen_width: int):

        self.__font_calc.update(self.__text_len, screen_width)
        self.__keyboard.update(screen_height, screen_width)
        self.__input_line.update(events)

    def draw(self, screen: pygame.Surface):
        self.__input_line.draw(screen, self.__font_calc.current_font_size())
        self.__random_line.draw(screen, self.__font_calc.current_font_size())
        self.__keyboard.draw(screen)
