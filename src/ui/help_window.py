import pygame
from pygame import Surface, Clock
from pygame.key import ScancodeWrapper
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.hands_animator import HandsAnimator
from ui.images_loader import ImagesLoader
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC
from pygame.typing import Point


class HelpWindow(WindowABC):

    def __init__(self, images_loader: ImagesLoader):
        super().__init__()

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH, relative_y_pos=0.025)
        self.__hands_animator = HandsAnimator(relative_y_pos=0.4, images_loader=images_loader)

    def update(self, keys: ScancodeWrapper):

        self.__hands_animator.update()
        self.__keyboard.update(keys)

        fingers_enum = self.__hands_animator.get_finger()
        is_visible = self.__hands_animator.is_visible()
        self.__keyboard.highlight_fingers_key(fingers_enum, is_visible)

    def draw(self, screen: Surface):
        self.__hands_animator.draw(screen)
        self.__keyboard.draw(screen)

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
                if event.type == pygame.KEYDOWN and event.key != pygame.K_F11:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button:
                    return

            if self.__hands_animator.is_repeat():
                return

            self.update(keys)
            self.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
