import pygame
from pygame.time import Clock
from pygame.event import Event
from common.common import get_resource_path
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
from ui.window_abc import WindowABC
from pygame.typing import Point
from pygame import Surface


class TypingWindow(WindowABC):

    def __init__(self, game_state: GameState):
        super().__init__()

        self.__game_state = game_state

        font_file_path = get_resource_path("src/_content/fonts/UbuntuMono-Regular.ttf")
        self.__font_calc = FontCalc(font_file_path)

        self.__text_len = 64
        text_generator = self.__game_state.generator

        time_provider = TimeProvider()
        self.__line_stats_calc = LineStatsCalc(time_provider)

        typing_errors = TypingErrors()

        mentor = Mentor()

        self.__keyboard = Keyboard(language=text_generator.keyboard_lang, relative_y_pos=0.4)

        self.__random_line = RandomLine(
            text_len=self.__text_len,
            errors=typing_errors,
            text_generator=text_generator,
            font_file_path=font_file_path,
            mentor=mentor
        )

        self.__input_line = InputLine(
            random_line=self.__random_line,
            keyboard=self.__keyboard,
            typing_errors=typing_errors,
            font_file_path=font_file_path,
            line_stats_calc=self.__line_stats_calc,
            mentor=mentor,
            game_state=self.__game_state
        )

    def update(self, events: list[Event], keys: ScancodeWrapper, screen_height: int, screen_width: int):
        self.__font_calc.update(self.__text_len, screen_width)
        self.__keyboard.update(screen_height, screen_width, keys)
        self.__input_line.update(events)
        self.__line_stats_calc.update(screen_height, screen_width)

    def draw(self, screen: Surface):
        self.__input_line.draw(screen, self.__font_calc.current_font_size(), self.__font_calc.current_text_width())
        self.__random_line.draw(screen, self.__font_calc.current_font_size(), self.__font_calc.current_text_width())
        self.__keyboard.draw(screen)
        self.__line_stats_calc.draw(screen)

    def show(
        self,
        screen: Surface,
        clock: Clock,
        min_screen_size: Point,
        max_screen_size: Point
    ):

        while True:
            screen.fill(BG_COLOR)

            keys = pygame.key.get_pressed()
            events = pygame.event.get()

            self.update_events(events, screen, min_screen_size, max_screen_size)

            if keys[pygame.K_ESCAPE]:
                return

            self.update(events, keys, screen.get_height(), screen.get_width())
            self.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
