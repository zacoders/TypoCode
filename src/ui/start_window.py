
import inspect
import sys
from typing import List, Tuple
from pygame import Rect
from pygame.event import Event
import pygame_gui
from pygame_gui.elements import UIButton, UISelectionList
from game_state import GameState
from pygame_gui import UIManager
import generators
from generators.generator_abc import GeneratorABC


class StartWindow:
    BUTTON_WIDTH = 0.2
    BUTTON_HEIGHT = 0.08

    SELECTION_LIST_WIDTH = 0.4
    SELECTION_LIST_HEIGHT = 0.4

    def __init__(self, game_state: GameState, manager: UIManager):

        self.__game_state = game_state
        self.__manager = manager

        self.__screen_width = 0
        self.__screen_height = 0

        self.__start_button_rel_rect = Rect((300, 900), (300, 140))
        self.__start_button = UIButton(
            relative_rect=self.__start_button_rel_rect,
            text="Start",
            manager=self.__manager,
        )

        self.__exit_button_rel_rect = Rect((300, 1100), (300, 140))
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
        self.__objects_zip = list(zip(
            [self.__select_list_rel_rect, self.__start_button_rel_rect, self.__exit_button_rel_rect],
            [self.__selection_list, self.__start_button, self.__exit_button],
            [
                (self.SELECTION_LIST_WIDTH, self.SELECTION_LIST_HEIGHT),
                (self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                (self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            ],
            [0.15, 0.65, 0.8]
        ))

    def __set_object_size(
        self,
        screen_width: int,
        screen_height: int,
        rel_rect: Rect,
        object: UIButton | UISelectionList,
        size: Tuple[float, float],
        pos_y: float
    ):
        width = screen_width * size[0]
        height = screen_height * size[1]

        rel_rect.x = screen_width // 2 - width // 2
        rel_rect.y = screen_height * pos_y

        object.set_dimensions((int(width), int(height)))
        object.set_position(rel_rect.topleft)
        object.rebuild()

    def update(self, events: List[Event], screen_width: int, screen_height: int):

        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width

            for rect, object, size, pos_y in self.__objects_zip:
                self.__set_object_size(screen_width, screen_height, rect, object, size, pos_y)

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

    def __gens_list_items(self):
        item = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, GeneratorABC):
                gen = generator_cls()
                item[gen.display_name] = gen
        return item
