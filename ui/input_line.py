
from pygame.font import Font
from pygame.event import Event
import pygame


class InputLine:

    def __init__(self):
        self.__text = ''
        self.__font_size = 100
        self.__text_color = (255, 255, 255)
        self.__text_line_color = (0, 0, 0)
        self.__font = Font("fonts/Inconsolata-Regular.ttf", self.__font_size)
        self.__current_char = 0
        self.__type_sound = pygame.mixer.Sound("sounds/typing-sound-02-229861.wav")
        self.__error_sound = pygame.mixer.Sound("sounds/error.mp3")

    def update(self, event: Event, rand_text_line_list):
        if event.key == pygame.K_BACKSPACE:
            if not self.__text:
                return
            self.__text = self.__text[:-1]
            if self.__current_char > 0:
                self.__current_char -= 1
        elif event.key == pygame.K_RETURN:
            self.__text = ""
            self.__current_char = 0
        else:
            if len(self.__text) >= len(rand_text_line_list):
                return

            if event.unicode == rand_text_line_list[self.__current_char]:
                self.__type_sound.play()
                self.__text += event.unicode
                self.__current_char += 1
            else:
                if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                    return
                self.__error_sound.play()

    def draw(self, screen: pygame.Surface):
        line_rect = pygame.Rect(
            0,
            screen.get_height() // 2,
            screen.get_width(),
            self.__font_size
        )
        pygame.draw.rect(screen, self.__text_line_color, line_rect)
        text = self.__font.render(self.__text, True, self.__text_color)
        screen.blit(text, line_rect)
