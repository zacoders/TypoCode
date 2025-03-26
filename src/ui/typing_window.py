from typing import Tuple
import pygame
from pygame.time import Clock
from pygame.event import Event
from common.common import update_events
from common.time_provider import TimeProvider
from consts import BG_COLOR, FPS
from services.line_stats_calc import LineStatsCalc
from services.mentor import Mentor
from typing_errors import TypingErrors
from pygame.key import ScancodeWrapper
from game_state import GameState
from ui.font_calc import FontCalc
from ui.input_line import InputLine
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class TypingWindow:

    def __init__(self, game_state: GameState):
        self.__game_state = game_state
        font_file_path = "src/_content/fonts/UbuntuMono-Regular.ttf"
        self.__text_len = 64
        text_generator = self.__game_state.generator
        time_provider = TimeProvider()
        self.__line_stats_calc = LineStatsCalc(time_provider)
        typing_errors = TypingErrors()
        mentor = Mentor()
        self.__keyboard = Keyboard(language=text_generator.keyboard_lang)
        self.__random_line = RandomLine(self.__text_len, typing_errors, text_generator, font_file_path, mentor)
        self.__input_line = InputLine(
            random_line=self.__random_line,
            keyboard=self.__keyboard,
            typing_errors=typing_errors,
            font_file_path=font_file_path,
            line_stats_calc=self.__line_stats_calc,
            mentor=mentor,
            game_state=self.__game_state
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

    def show(self, screen: pygame.Surface, clock: Clock, min_screen_size: Tuple[int, int]):

        while self.__game_state.is_started:
            screen.fill(BG_COLOR)

            keys: ScancodeWrapper = pygame.key.get_pressed()

            events = pygame.event.get()

            update_events(events, self.__game_state, keys, screen, min_screen_size)

            self.update(events, keys, screen.get_height(), screen.get_width())
            self.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
