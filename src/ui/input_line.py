from pygame.font import Font
from pygame.event import Event
import pygame
from game_state import GameState
from services.keyboard_service import KeyboardService
from stats.line_stats_calc import LineStatsCalc
from typing_errors import TypingErrors
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class InputLine:

    def __init__(
        self,
        random_line: RandomLine,
        keyboard: Keyboard,
        typing_errors: TypingErrors,
        font_file_path: str,
        line_stats_calc: LineStatsCalc,
        game_state: GameState
    ):

        self.__game_state = game_state

        self.__random_line = random_line
        self.__keyboard = keyboard
        self.__line_stats_calc = line_stats_calc

        self.__text = ''
        self.__cursor_symbol = "\u258F"

        self.__prev_font_size = 100

        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)

        self.__font_file_path = font_file_path
        self.__font = Font(font_file_path, self.__prev_font_size)

        self.__typing_errors = typing_errors

        self.__type_sound = pygame.mixer.Sound("src/_content/sounds/typing-sound-02-229861.wav")
        self.__error_sound = pygame.mixer.Sound("src/_content/sounds/error.mp3")

        self.__interactive_buttons = [pygame.K_TAB,
                                      pygame.K_CAPSLOCK,
                                      pygame.K_LSHIFT,
                                      pygame.K_LCTRL,
                                      pygame.K_LALT,
                                      pygame.K_RALT,
                                      pygame.K_RCTRL,
                                      pygame.K_RSHIFT,
                                      pygame.K_RETURN,
                                      pygame.K_BACKSPACE]

        self.__keyboard_service = KeyboardService()

    def __get_word(self, pos: int) -> str:
        words = self.__random_line.get_text().split()
        count = 0
        for word in words:
            if count <= pos < count + len(word):
                return word
            count += len(word) + 1  # +1 for space
        return ""

    def update(self, events: list[Event]):
        rand_text = self.__random_line.get_text()

        if len(self.__text) >= len(rand_text):
            self.__random_line.next_line()
            self.__text = ''
            return

        current_char_pos = len(self.__text)
        current_char = rand_text[current_char_pos]

        self.__keyboard.highlight_key(current_char)

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            if event.key in self.__interactive_buttons:
                return

            if not self.__text:
                self.__line_stats_calc.start()

            unicode_char = self.__keyboard_service.get_char_from_key(event.scancode, self.__game_state.generator.keyboard_lang)
            print(unicode_char)

            if unicode_char == current_char:
                self.__type_sound.play()
                self.__line_stats_calc.symbol_typed(is_error=False)
                self.__text += unicode_char
            else:
                if unicode_char:
                    word = self.__get_word(current_char_pos)
                    self.__typing_errors.add_errors(current_char, word)
                self.__line_stats_calc.symbol_typed(is_error=True)
                self.__error_sound.play()

            if len(self.__text) == self.__random_line.text_len:
                self.__line_stats_calc.stop()

        # print(self.__line_stats_calc.get_stats())

    def draw(self, screen: pygame.Surface, font_size: int, text_width: int):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 3,
            screen.get_width(),
            font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        if self.__prev_font_size != font_size:
            self.__font = Font(self.__font_file_path, font_size)
            self.__prev_font_size = font_size

        text = self.__font.render(self.__text + self.__cursor_symbol, True, self.__text_color)
        diff_x = (screen.get_width() - text_width) / 2
        text_pos = (diff_x, line_rect.y)
        screen.blit(text, text_pos)

    def get_errors(self):
        return self.__typing_errors
