import pygame

from pygame import Surface


class Blur:

    def __init__(self, screen: Surface):
        self.__screen = screen
        self.__blur_sc = pygame.surface.Surface((self.__screen.get_width(), self.__screen.get_height()))

    def draw(self):
        self.__blur_sc.fill((0, 0, 0))
        self.__blur_sc.set_alpha(180)
        self.__screen.blit(self.__blur_sc, (0, 0))
