import sys
from pygame import Surface
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC
from ui.menus.generator_menu import GeneratorMenu


class MainMenu(ScreenABC):

    def __init__(self, game_state: GameState, screen: Surface):
        super().__init__(screen)

        self.__game_state = game_state

        self.__screen = screen

        self.__button_size = (370, 70)

        self.add_button(Button(self.__button_size, 'Change_Language_Dictionary', action=self.generators_screen))
        self.add_button(Button(self.__button_size, 'Start', action=self.start))
        self.add_button(Button(self.__button_size, 'Exit', action=lambda: sys.exit()))

    def start(self):
        self.__game_state.active_screen = None

    def generators_screen(self):
        self.__game_state.active_screen = GeneratorMenu(self.__game_state, self, self.__screen)
