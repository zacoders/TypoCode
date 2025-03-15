
import inspect
import sys
from pygame import Surface
from pygame import Rect
import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from game_state import GameState
from pygame_gui import UIManager

import generators
from generators.base import BaseGenerator


class ButtonsWindow:

    def __init__(self, game_state: GameState, manager: UIManager, screen: Surface):

        self.__game_state = game_state
        self.__manager = manager

        self.__main_menu_buttons = {
            "Start": self.__start,
            "Exit": self.__exit
        }

        self.__generators_list_items = self.__gens_list_items()
        self.__selection_list = pygame_gui.elements.UISelectionList(
            relative_rect=Rect(100, 100, 200, 100),
            item_list=list(self.__generators_list_items.keys()),
            manager=manager
        )

    def update(self):
        ...

    def __gens_list_items(self):
        item = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, BaseGenerator):
                name = generator_cls.__name__
                item[name] = lambda gen = generator_cls(): self.__set_generator(gen)
        return item

    def __start(self):
        self.__game_state.active_screen = None

    def __exit(self):
        sys.exit()

    def __set_generator(self, generator: BaseGenerator):
        self.__game_state.generator = generator
        print(f"Выбран генератор: {self.__game_state.generator.__name__}")
