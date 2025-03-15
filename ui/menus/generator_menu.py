from pygame import Surface
import inspect

import pygame
import pygame_gui
from pygame_gui import UIManager
import generators
from generators.base import BaseGenerator
from game_state import GameState
from ui.menus.basic.button_manager import ButtonManager


class GeneratorMenu(ButtonManager):

    def __init__(self, game_state: GameState, manager: UIManager, parent_screen: ButtonManager, screen: Surface):

        self.__parent_screen = parent_screen
        self.__game_state = game_state
        self.__buttons_size = (300, 70)

        buttons = self.__create_buttons_from_generators(generators, manager)

        super().__init__(screen, manager, buttons)

    def __create_buttons_from_generators(self, generators, manager):
        y_offset = 150
        buttons = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, BaseGenerator):
                button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((150, y_offset), self.__buttons_size),
                    text=name,
                    manager=manager
                )
                y_offset += self.__buttons_size[1] + 20
                buttons[button] = lambda gen = generator_cls: self.set_generator(gen)
        return buttons

    def set_generator(self, generator: BaseGenerator):
        self.__game_state.generator = generator
        print(f"Выбран генератор: {self.__game_state.generator.__name__}")
        self.__game_state.active_screen = self.__parent_screen
