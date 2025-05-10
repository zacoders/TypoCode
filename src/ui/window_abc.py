from abc import ABC
import sys
from typing import List
import pygame
from pygame import Event, Surface
from pygame.typing import Point


class WindowABC(ABC):

    __prev_screen_size = (0, 0)
    __is_fullscreen = False

    def update_events(
        self,
        events: List[Event],
        screen: Surface,
        min_screen_size: Point,
        max_screen_size: Point
    ):
        min_width, min_height = min_screen_size

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                if WindowABC.__is_fullscreen:
                    screen = pygame.display.set_mode(self.__prev_screen_size, pygame.RESIZABLE)
                    WindowABC.__is_fullscreen = False
                else:
                    WindowABC.__prev_screen_size = screen.get_size()
                    screen = pygame.display.set_mode(max_screen_size, pygame.FULLSCREEN)
                    WindowABC.__is_fullscreen = True

        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

            if event.type == pygame.VIDEORESIZE and not WindowABC.__is_fullscreen:
                new_width = event.w if event.w > min_width else min_width
                new_height = event.h if event.h > min_height else min_height
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
