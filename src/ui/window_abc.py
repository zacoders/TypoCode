
from abc import ABC
import sys
from typing import List, Tuple
import pygame
from pygame import Event, Surface
from pygame.key import ScancodeWrapper


class WindowABC(ABC):

    def __init__(self):
        self.__prev_screen_size = (0, 0)
        self.__is_fullscreen = False

    def update_events(
        self,
        keys: ScancodeWrapper,
        events: List[Event],
        screen: Surface,
        min_screen_size: Tuple[int, int],
        max_screen_size: Tuple[int, int]
    ):
        min_width, min_height = min_screen_size

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE and not self.__is_fullscreen:
                new_width = event.w if event.w > min_width else min_width
                new_height = event.h if event.h > min_height else min_height
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

            if event.type == pygame.KEYDOWN and keys[pygame.K_F11]:
                if screen.get_size() != max_screen_size:
                    self.__prev_screen_size = screen.get_size()
                    new_screen_size = max_screen_size
                    self.__is_fullscreen = True
                else:
                    new_screen_size = self.__prev_screen_size
                    self.__is_fullscreen = False

                screen = pygame.display.set_mode(
                    new_screen_size,
                    pygame.FULLSCREEN if self.__is_fullscreen else pygame.RESIZABLE
                )
