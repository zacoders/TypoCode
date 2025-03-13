from pygame import Surface
from generators.c_sharp import CSharpGenerator
from generators.english import EnglishGenerator
from generators.python import PythonGenerator
from generators.russian import RussianGenerator
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC


class MainMenu(ScreenABC):

    def __init__(self, game_state: GameState, screen: Surface):
        super().__init__(screen)

        self.__game_state = game_state

        self.__current_index = 0
        self.__generators = [
            PythonGenerator(),
            CSharpGenerator(),
            RussianGenerator(),
            EnglishGenerator()
        ]

        self.add_button(Button(1, f'Language_Dictionary', action=self.toggle_keyboard_lang))
        self.add_button(Button(1, 'Start', action=self.start))

    def start(self):
        GameState.active_screen = None
        print(f"{GameState.active_screen=}")
        print(f"{GameState.generator=}")
        print("Запуск игры...")

    def toggle_keyboard_lang(self):
        self.__current_index += 1
        if self.__current_index >= len(self.__generators):
            self.__current_index = 0

        generator = self.__generators[self.__current_index]
        self.__game_state.generator = generator

        print(generator)
