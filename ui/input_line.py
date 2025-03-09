
from pygame.font import Font
from pygame.event import Event
import pygame

from errors import Errors
from ui.keyboard import Keyboard
from ui.random_line import RandomLine


class InputLine:

    def __init__(self, random_line: RandomLine, keyboard: Keyboard):

        self.__random_line = random_line
        self.__keyboard = keyboard

        self.__text = ''
        self.__cursor_symbol = "\u258F"

        self.__prev_font_size = 100

        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)

        self.__font = Font("fonts/Inconsolata-Regular.ttf", self.__prev_font_size)

        self.__errors = Errors()

        self.__type_sound = pygame.mixer.Sound("sounds/typing-sound-02-229861.wav")
        self.__error_sound = pygame.mixer.Sound("sounds/error.mp3")

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

            if event.unicode == current_char:
                self.__type_sound.play()
                self.__text += event.unicode
            else:
                if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK]:
                    return

                if event.unicode:
                    word = self.__get_word(current_char_pos)
                    self.__errors.add_errors(current_char, word)

                self.__error_sound.play()

    def draw(self, screen: pygame.Surface, font_size: int):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 3,
            screen.get_width(),
            font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        if self.__prev_font_size != font_size:
            self.__font = Font("fonts/Inconsolata-Regular.ttf", font_size)
            self.__prev_font_size = font_size

        text = self.__font.render(self.__text + self.__cursor_symbol, True, self.__text_color)
        screen.blit(text, line_rect)
