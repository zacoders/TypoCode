
import inspect
import sys
from typing import List
from pygame import Rect
from pygame.event import Event
import pygame_gui
from game_state import GameState
from pygame_gui import UIManager
import generators
from generators.base import BaseGenerator


class ButtonsWindow:

    def __init__(self, game_state: GameState, manager: UIManager):

        self.__game_state = game_state

        self.__start_button = pygame_gui.elements.UIButton(
            relative_rect=Rect((150, 450), (300, 70)),
            text="Start",
            manager=manager,
        )

        self.__exit_button = pygame_gui.elements.UIButton(
            relative_rect=Rect((150, 550), (300, 70)),
            text="Exit",
            manager=manager)

        self.__generators_list_items = self.__gens_list_items()

        generator_names = list(self.__generators_list_items.keys())
        self.__selection_list = pygame_gui.elements.UISelectionList(
            relative_rect=Rect(100, 100, 500, 300),
            item_list=generator_names,
            manager=manager,
            default_selection=generator_names[0]
        )

    def update(self, events: List[Event]):
        for event in events:
            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                selected_item = self.__selection_list.get_single_selection()
                if selected_item:
                    if selected_item in self.__generators_list_items:
                        self.__generators_list_items[selected_item]()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.__start_button:
                    self.__game_state.is_started = True
                if event.ui_element == self.__exit_button:
                    sys.exit()

    def __gens_list_items(self):
        item = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, BaseGenerator):
                name = generator_cls.__name__
                item[name] = lambda gen = generator_cls: self.__set_generator(gen)
        return item

    def __set_generator(self, generator: type):
        self.__game_state.generator = generator()
        print(f"Выбран генератор: {generator.__name__}")
