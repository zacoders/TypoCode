

from typing import Tuple
import pygame
from pygame import Surface, Clock
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.hands_animator import HandsAnimator
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC


class HelpWindow(WindowABC):

    def __init__(self):
        super().__init__()

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH, relative_y_pos=0.0)
        self.__hands_animator = HandsAnimator()

    def show(self, screen: Surface, clock: Clock, min_screen_size: Tuple[int, int], max_screen_size: Tuple[int, int]):
        while True:
            screen.fill(BG_COLOR)

            keys = pygame.key.get_pressed()
            events = pygame.event.get()

            self.update_events(keys, events, screen, min_screen_size, max_screen_size)

            if keys[pygame.K_ESCAPE]:
                return
            elif keys[pygame.K_RETURN]:
                return

            self.__hands_animator.update()
            self.__keyboard.update(screen.height, screen.width, keys)

            fingers_enum = self.__hands_animator.get_finger_enum()
            self.__keyboard.highlight_fingers_key(fingers_enum)

            self.__hands_animator.draw(screen)
            self.__keyboard.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
