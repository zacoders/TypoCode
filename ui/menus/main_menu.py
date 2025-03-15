import sys
from pygame import Surface
import pygame
from pygame_gui import UIManager
import pygame_gui
from game_state import GameState
from ui.menus.basic.button_manager import ButtonManager
from ui.menus.generator_menu import GeneratorMenu


class MainMenu(ButtonManager):

    def __init__(self, game_state: GameState, manager: UIManager, screen: Surface):

        self.__game_state = game_state
        self.__screen = screen
        self.__manager = manager

        self.__button_size = (370, 70)

        self.__change_gen_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((150, 150), self.__button_size),
            text="Change_Language_Dictionary",
            manager=manager)

        self.__start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((150, 350), self.__button_size),
            text="Start",
            manager=manager)

        self.__exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((150, 550), self.__button_size),
            text="Exit",
            manager=manager)

        buttons = {
            self.__change_gen_button: self.gens_screen,
            self.__start_button: self.start,
            self.__exit_button: self.exit
        }

        super().__init__(screen, manager, buttons)

    def start(self):
        self.__game_state.active_screen = None

    def gens_screen(self):
        self.__game_state.active_screen = GeneratorMenu(self.__game_state, self.__manager, self, self.__screen)

    def exit(self):
        sys.exit()
