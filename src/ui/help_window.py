

from typing import Tuple
import pygame
from pygame import Surface, Clock
from common.common import get_resource_path
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.finger_animator import FingerAnimator
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC


class HelpWindow(WindowABC):

    def __init__(self):
        super().__init__()

        arms_image = pygame.image.load(
            get_resource_path("src/_content/images/arms/arms.png"))
        self.__arms_image = pygame.transform.scale(
            arms_image, (arms_image.width // 1.1, arms_image.height // 1.1))

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH, relative_y_pos=0.0)
        self.__finger_animator = FingerAnimator()

    def draw(self, screen: Surface):
        screen.blit(
            self.__arms_image,
            (
                screen.get_width() // 2 - self.__arms_image.width // 2,
                screen.get_height() - self.__arms_image.height
            )
        )

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

            self.draw(screen)

            self.__finger_animator.update()
            self.__keyboard.update(screen.height, screen.width, keys)

            self.__finger_animator.draw(screen, self.__arms_image.size)
            finger_enum = self.__finger_animator.get_finger_enum()
            
            self.__keyboard.highlight_fingers_key(finger_enum)
            self.__keyboard.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
