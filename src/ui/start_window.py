import inspect
import sys
from typing import List, Tuple
from pygame import Rect, Surface
import pygame
from pygame.time import Clock
from pygame.event import Event
import pygame_gui
from pygame_gui.elements import UISelectionList
from consts import BG_COLOR, FPS
from state import State
import generators
from generators.generator_abc import GeneratorABC
from ui.theme_config import get_theme_path
from ui.window_abc import WindowABC
from pygame.typing import Point


class StartWindow(WindowABC):

    def __init__(self, state: State):
        super().__init__()

        self.__state = state

        self.__screen_width = 0
        self.__screen_height = 0

        self.__generators_list_items = self.__gens_list_items()
        self.__generator_names = list(self.__generators_list_items.keys())

        self.__reload_objects((self.__screen_width, self.__screen_height))

    def __reload_objects(self, screen_size: Tuple[int, int]):
        self.__manager = pygame_gui.UIManager(
            screen_size,
            enable_live_theme_updates=True,
            theme_path=get_theme_path()
        )

        list_width = int(screen_size[0] * 0.7)
        list_height = int(screen_size[1] * 0.7)
        list_width = min(list_width, 1200)
        list_height = min(list_height, 940)

        pos_x = screen_size[0] // 2 - list_width // 2
        pos_y = screen_size[1] // 2 - list_height // 2

        self.__selection_list = UISelectionList(
            relative_rect=Rect(pos_x, pos_y, list_width, list_height),
            item_list=self.__generator_names,
            manager=self.__manager
        )

    def __update(self, events: List[Event], screen_width: int, screen_height: int):
        if self.__screen_height != screen_height or self.__screen_width != screen_width:
            self.__screen_height = screen_height
            self.__screen_width = screen_width
            self.__reload_objects((self.__screen_width, self.__screen_height))

        for event in events:
            if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                selected_item = self.__selection_list.get_single_selection()
                if selected_item and selected_item in self.__generators_list_items:
                    self.__state.generator = self.__generators_list_items[selected_item]

    def __gens_list_items(self):
        item = {}
        for _, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, GeneratorABC):
                gen = generator_cls()
                item[gen.display_name] = gen
        return item

    def show(
        self,
        screen: Surface,
        start_screen_size: Point,
        clock: Clock,
        min_screen_size: Point,
        max_screen_size: Point
    ):
        self.__selection_list.rebuild()
        while True:
            screen.fill(BG_COLOR)

            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            self.update_events(events, screen, min_screen_size, max_screen_size)

            self.__update(events, screen.get_width(), screen.get_height())

            for event in events:
                if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                    return
                if event.type == pygame.KEYDOWN and keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            if start_screen_size != screen.size:
                self.__manager.set_window_resolution(screen.size)

            for event in events:
                self.__manager.process_events(event)

            self.__manager.draw_ui(screen)

            time_delta = clock.tick(FPS) / 1000.0
            self.__manager.update(time_delta)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
