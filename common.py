import sys
from typing import List
from pygame.event import Event
from pygame import Surface
import pygame


def update_events(events: List[Event], keys, screen: Surface):
    screen = screen
    for event in events:
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.w, event.h
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
