
from pygame.font import Font
from pygame.event import Event
import pygame

from ui.random_line import RandomLine


class InputLine:

    def __init__(self, random_line: RandomLine):

        self.__random_line = random_line

        self.__text = ''

        self.__prev_font_size = 100

        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)

        self.__font = Font("fonts/Inconsolata-Regular.ttf", self.__prev_font_size)

        self.__type_sound = pygame.mixer.Sound("sounds/typing-sound-02-229861.wav")
        self.__error_sound = pygame.mixer.Sound("sounds/error.mp3")

    def update(self, event: Event):
        rand_text = self.__random_line.get_text()
        if len(self.__text) >= len(rand_text):
            self.__random_line.next_line()
            self.__text = ''
            return

        current_char = len(self.__text)
        if event.unicode == rand_text[current_char]:
            self.__type_sound.play()
            self.__text += event.unicode
        else:
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK]:
                return
            self.__error_sound.play()

    def draw(self, screen: pygame.Surface, font_size: int):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 2,
            screen.get_width(),
            font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        if self.__prev_font_size != font_size:
            if font_size > 5:
                self.__font = Font("fonts/Inconsolata-Regular.ttf", font_size)
                self.__prev_font_size = font_size
            else:
                return

        text = self.__font.render(self.__text, True, self.__text_color)
        screen.blit(text, line_rect)
