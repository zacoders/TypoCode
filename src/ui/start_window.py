import inspect
from typing import List, Tuple
from pygame import Rect, Surface
import pygame
from pygame.time import Clock
from pygame.event import Event
import pygame_gui
from pygame_gui.elements import UISelectionList
from common.common import update_events
from consts import BG_COLOR, FPS
from game_state import GameState
from pygame_gui import UIManager
import generators
from generators.generator_abc import GeneratorABC


class StartWindow:

    def __init__(self, game_state: GameState, manager: UIManager):
        self.__game_state = game_state
        self.__manager = manager

        self.__screen_width = 0
        self.__screen_height = 0

        self.__generators_list_items = self.__gens_list_items()
        self.__generator_names = list(self.__generators_list_items.keys())

        self.__selection_list = UISelectionList(
            relative_rect=Rect(200, 200, 1200, 720),
            item_list=self.__generator_names,
            manager=self.__manager,
            default_selection=self.__generator_names[0]
        )

    def __update(self, events: List[Event], screen_width: int, screen_height: int):
        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width

            pos_x = screen_width // 2 - self.__selection_list.relative_rect.width // 2
            pos_y = screen_height // 2 - self.__selection_list.relative_rect.height // 2

            self.__selection_list.set_position((pos_x, pos_y))
            self.__selection_list.rebuild()

        for event in events:
            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                selected_item = self.__selection_list.get_single_selection()
                self.__game_state.is_started = True
                if selected_item and selected_item in self.__generators_list_items:
                    self.__game_state.generator = self.__generators_list_items[selected_item]

    def __gens_list_items(self):
        item = {}
        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, GeneratorABC):
                gen = generator_cls()
                item[gen.display_name] = gen
        return item

    def show(self, screen: Surface, start_screen_size: Tuple[int, int], clock: Clock, min_screen_size: Tuple[int, int]):

        while not self.__game_state.is_started:
            screen.fill(BG_COLOR)

            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            update_events(events, self.__game_state, keys, screen, min_screen_size)

            time_delta = clock.tick(FPS) / 1000.0

            self.__update(events, screen.get_width(), screen.get_height())

            if start_screen_size != screen.size:
                self.__manager.set_window_resolution(screen.size)

            for event in events:
                self.__manager.process_events(event)

            self.__manager.draw_ui(screen)
            self.__manager.update(time_delta)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
