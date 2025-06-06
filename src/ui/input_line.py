from pygame.font import Font
from pygame.event import Event
import pygame
from common.common import get_resource_path
from state import State
from services.keyboard_service import KeyboardService
from services.line_stats_calc import LineStatsCalc
from services.mentor import Mentor
from common.typing_errors import TypingErrors
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
        state: State,
        mentor: Mentor
    ):

        self.__state = state

        self.__random_line = random_line
        self.__keyboard = keyboard
        self.__line_stats_calc = line_stats_calc
        self.__mentor = mentor

        self.__text = ''
        self.__error_symbol = ''

        self.__prev_font_size = 100

        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)

        self.__font_file_path = font_file_path
        self.__font = Font(font_file_path, self.__prev_font_size)

        self.__typing_errors = typing_errors

        self.__type_sound = pygame.mixer.Sound(get_resource_path("src/_content/sounds/typing-sound-02-229861.wav"))
        self.__error_sound = pygame.mixer.Sound(get_resource_path("src/_content/sounds/error.mp3"))

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
        prev_char = rand_text[current_char_pos - 1 if current_char_pos > 0 else 0]
        word = self.__get_word(current_char_pos)

        self.__keyboard.highlight_key(current_char, prev_char, word)

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            unicode_char = self.__keyboard_service.get_char_from_key(
                event.scancode, self.__state.generator.keyboard_lang)

            if unicode_char == '':
                continue

            if not self.__text:
                self.__line_stats_calc.start()

            if unicode_char == current_char:
                self.__type_sound.play()
                self.__line_stats_calc.symbol_typed(is_error=False, char=unicode_char)
                self.__text += unicode_char
                self.__error_symbol = ''
            else:
                if unicode_char:
                    word = self.__get_word(current_char_pos)
                    self.__typing_errors.add_errors(current_char, word)
                self.__line_stats_calc.symbol_typed(is_error=True, char=unicode_char)
                self.__error_sound.play()
                self.__error_symbol = unicode_char

            if len(self.__text) == self.__random_line.text_len:
                self.__line_stats_calc.stop()
                self.__mentor.update_stats(self.__line_stats_calc.get_stats())

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

        diff_x = (screen.get_width() - text_width) / 2
        text_pos = (diff_x, line_rect.y)

        font_text_width, _ = self.__font.size(self.__text)

        cursor_rect = pygame.Rect(
            text_pos[0] + font_text_width,
            line_rect.y,
            self.__font.size('0')[1] / 16,  # 1/16 of font size
            line_rect.height
        )

        if self.__error_symbol and self.__error_symbol != ' ':
            text = self.__font.render(self.__text + self.__error_symbol, True, (200, 0, 0))
            screen.blit(text, text_pos)
            text2 = self.__font.render(self.__text, True, self.__text_color)
            screen.blit(text2, text_pos)
        elif self.__error_symbol == ' ':
            text = self.__font.render(self.__text, True, self.__text_color)
            screen.blit(text, text_pos)
            pygame.draw.rect(screen, (200, 0, 0), cursor_rect)
        else:
            text = self.__font.render(self.__text, True, self.__text_color)
            screen.blit(text, text_pos)
            pygame.draw.rect(screen, self.__text_color, cursor_rect)
