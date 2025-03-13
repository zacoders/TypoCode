import pygame
from pygame.event import Event
from errors import Errors
from game_state import GameState
from ui.font_calc import FontCalc
from ui.input_line import InputLine
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class MainWindow:

    def __init__(self, game_state: GameState):
        font_file_path = "fonts/UbuntuMono-Regular.ttf"
        self.__text_len = 64
        self.__text_generator = game_state.generator
        self.__keyboard = Keyboard(language=self.__text_generator.keyboard_lang)
        self.__errors = Errors()
        self.__random_line = RandomLine(self.__text_len, self.__errors, self.__text_generator, font_file_path)
        self.__input_line = InputLine(self.__random_line, self.__keyboard, self.__errors, font_file_path)
        self.__font_calc = FontCalc(font_file_path)

    def update(self, events: list[Event], screen_height: int, screen_width: int):

        self.__font_calc.update(self.__text_len, screen_width)
        self.__keyboard.update(screen_height, screen_width)
        self.__input_line.update(events)

    def draw(self, screen: pygame.Surface):
        self.__input_line.draw(screen, self.__font_calc.current_font_size())
        self.__random_line.draw(screen, self.__font_calc.current_font_size())
        self.__keyboard.draw(screen)
