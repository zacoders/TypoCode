

import pygame
from pygame import Surface, Clock
from pygame.key import ScancodeWrapper
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.hands_animator import HandsAnimator
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC
from pygame.typing import Point


class HelpWindow(WindowABC):

    def __init__(self):
        super().__init__()

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH)
        self.__hands_animator = HandsAnimator()

        self.__y_distance = 20

    def update(self, screen_width: int, screen_height: int, keys: ScancodeWrapper):
        
        print(f'hands_animator_image_height = {self.__hands_animator.get_image_height()}, keyboard_height = {self.__keyboard.get_height()}')

        total_height = self.__get_total_objs_height(
            self.__y_distance,
            self.__hands_animator.get_image_height(),
            self.__keyboard.get_height()
        )
        
        relative_y_pos = abs((screen_height - total_height) / 2 / screen_height)

        self.__hands_animator.update()
        self.__keyboard.update(screen_height, screen_width, keys, relative_y_pos)

        fingers_enum = self.__hands_animator.get_finger_enum()
        visible_stage = self.__hands_animator.get_visible_stage()
        self.__keyboard.highlight_fingers_key(fingers_enum, visible_stage)

    def draw(self, screen: Surface):
        self.__hands_animator.draw(screen, self.__keyboard.get_bottom_y(), self.__y_distance)
        self.__keyboard.draw(screen)

    def __get_total_objs_height(
        self,
        y_distance: int,
        hands_height: int,
        keyboard_height: int
    ) -> int:

        return hands_height + y_distance + keyboard_height

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

            if self.__hands_animator.get_repeat_stage():
                return

            self.update(screen.width, screen.height, keys)
            self.draw(screen)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
