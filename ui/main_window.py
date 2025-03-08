import pygame
from pygame.event import Event
from pygame.font import Font
from text_generator import TextGenerator
from ui.input_line import InputLine
from ui.random_line import RandomLine


class MainWindow:

    def __init__(self):
        self.__random_line = RandomLine()
        self.__input_line = InputLine()

    def update(self, events: list[Event]):
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                continue

            self.__input_line.update(event)

    def draw(self, screen: pygame.Surface):
        self.__input_line.draw(screen)
        self.__random_line.draw(screen)
