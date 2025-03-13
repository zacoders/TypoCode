from pygame import Surface
from generators.c_sharp import CSharpGenerator
from generators.python import PythonGenerator
from generators.russian import RussianGenerator
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC


class MainMenu(ScreenABC):

    def __init__(self, generator, game_state: GameState, screen: Surface):
        super().__init__(screen)

        self.__game_state = game_state

        self.__generators = [PythonGenerator(), CSharpGenerator(), RussianGenerator()]
        self.__generator = generator

        self.add_button(Button(1, f'Language_Dictionary', action=self.toggle_keyboard_lang))
        self.add_button(Button(1, 'Start', action=self.start))

    def start(self):
        GameState.generator = self.__generator
        GameState.active_screen = None
        print(f"{GameState.active_screen=}")
        print(f"{GameState.generator=}")
        print("Запуск игры...")

    def toggle_keyboard_lang(self):
        current_index = next(
            (i for i, gen in enumerate(
                self.__generators) if isinstance(
                self.__generator, type(gen))), -1)
        if current_index == -1:
            return

        next_index = (current_index + 1) % len(self.__generators)
        self.__generator = self.__generators[next_index]
        self.__game_state.generator = self.__generator

        print(self.__generator)
