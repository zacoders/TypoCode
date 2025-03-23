import pygame
from pygame.event import Event
from common.time_provider import TimeProvider
from stats.line_stats_calc import LineStatsCalc
from typing_errors import TypingErrors
from pygame.key import ScancodeWrapper
from game_state import GameState
from ui.font_calc import FontCalc
from ui.input_line import InputLine
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class TypingWindow:

    def __init__(self, game_state: GameState):
        font_file_path = "src/_content/fonts/UbuntuMono-Regular.ttf"
        self.__text_len = 64

        text_generator = game_state.generator
        time_provider = TimeProvider()
        self.__line_stats_calc = LineStatsCalc(time_provider)
        typing_errors = TypingErrors()

        self.__keyboard = Keyboard(language=text_generator.keyboard_lang)
        self.__random_line = RandomLine(self.__text_len, typing_errors, text_generator, font_file_path)
        self.__input_line = InputLine(
            random_line=self.__random_line,
            keyboard=self.__keyboard,
            typing_errors=typing_errors,
            font_file_path=font_file_path,
            line_stats_calc=self.__line_stats_calc,
            game_state=game_state
        )
        self.__font_calc = FontCalc(font_file_path)

    def update(self, events: list[Event], keys: ScancodeWrapper, screen_height: int, screen_width: int):
        self.__font_calc.update(self.__text_len, screen_width)
        self.__keyboard.update(screen_height, screen_width, keys)
        self.__input_line.update(events)
        self.__line_stats_calc.update(screen_height, screen_width)

    def draw(self, screen: pygame.Surface):
        self.__input_line.draw(screen, self.__font_calc.current_font_size(), self.__font_calc.current_text_width())
        self.__random_line.draw(screen, self.__font_calc.current_font_size(), self.__font_calc.current_text_width())
        self.__keyboard.draw(screen)
        self.__line_stats_calc.draw(screen)
