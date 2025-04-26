

import pygame
from pygame import Font, Surface, Clock
from common.common import get_resource_path
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.font_calc import FontCalc
from ui.hands_animator import HandsAnimator
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC
from pygame.typing import Point


class HelpWindow(WindowABC):

    def __init__(self):
        super().__init__()

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH, relative_y_pos=0.01)
        self.__hands_animator = HandsAnimator()

        self.__font_file_path = get_resource_path("src/_content/fonts/UbuntuMono-Regular.ttf")

        self.__font_calc = FontCalc(self.__font_file_path)

        self.__str_text = "press ENTER to skip"
        self.__reload_text()
        self.__text_len = len(self.__str_text)

    def __reload_text(self):
        self.__font = Font(self.__font_file_path, self.__font_calc.current_font_size())
        self.__text = self.__font.render(self.__str_text, True, (255, 255, 255))

    def update(self, screen_width: int):
        self.__font_calc.update(self.__text_len, screen_width // 5)
        self.__reload_text()

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

            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            self.update(screen.width)

            self.__hands_animator.update()
            self.__keyboard.update(screen.height, screen.width, keys)

            fingers_enum = self.__hands_animator.get_finger_enum()
            self.__keyboard.highlight_fingers_key(fingers_enum, self.__hands_animator.get_visible_stage())

            self.__hands_animator.draw(screen)
            self.__keyboard.draw(screen)

            screen.blit(
                self.__text,
                (
                    screen.width - self.__text.width - 5,
                    screen.height - self.__text.height - 5
                )
            )

            if self.__hands_animator.get_repeat_stage():
                return

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
