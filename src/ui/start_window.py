
import inspect
import sys
from typing import List
from pygame import Rect, Surface
from pygame.event import Event
import pygame_gui
from pygame_gui.elements import UIButton, UISelectionList
from game_state import GameState
from pygame_gui import UIManager
import generators
from generators.generator_abc import GeneratorABC


class StartWindow:

    def __init__(self, game_state: GameState, manager: UIManager):

        self.__game_state = game_state
        self.__manager = manager

        self.__start_button_rel_rect = Rect((300, 900), (600, 140))
        self.__start_button = UIButton(
            relative_rect=self.__start_button_rel_rect,
            text="Start",
            manager=self.__manager,
        )

        self.__exit_button_rel_rect = Rect((300, 1100), (600, 140))
        self.__exit_button = UIButton(
            relative_rect=self.__exit_button_rel_rect,
            text="Exit",
            manager=self.__manager
        )

        self.__generators_list_items = self.__gens_list_items()
        self.__select_list_rel_rect = Rect(200, 200, 1000, 600)
        self.__generator_names = list(self.__generators_list_items.keys())

        self.__selection_list = UISelectionList(
            relative_rect=self.__select_list_rel_rect,
            item_list=self.__generator_names,
            manager=self.__manager,
            default_selection=self.__generator_names[0]
        )

        self.__rel_rects = [self.__start_button_rel_rect, self.__exit_button_rel_rect, self.__select_list_rel_rect]
        self.__objects = [self.__start_button, self.__exit_button, self.__selection_list]

    def update(self, events: List[Event], screen: Surface):

        for rect, object in zip(self.__rel_rects, self.__objects):
            self.__set_buttons_to_center(rect, object, screen)

        for event in events:
            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                selected_item = self.__selection_list.get_single_selection()
                if selected_item:
                    if selected_item in self.__generators_list_items:
                        self.__game_state.generator = self.__generators_list_items[selected_item]
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.__start_button:
                    self.__game_state.is_started = True
                if event.ui_element == self.__exit_button:
                    sys.exit()

    def __set_buttons_to_center(self, rel_rect: Rect, object: UIButton | UISelectionList, screen: Surface):
        rel_rect.centerx = screen.get_width() // 2
        object.set_dimensions(rel_rect.size)
        object.set_position(rel_rect.topleft)

    def __gens_list_items(self):
        item = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, GeneratorABC):
                gen = generator_cls()
                item[gen.display_name] = gen
        return item
