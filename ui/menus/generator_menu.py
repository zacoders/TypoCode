from pygame import Surface
from generators.base import BaseGenerator
from generators.c_sharp import CSharpGenerator
from generators.english import EnglishGenerator
from generators.python import PythonGenerator
from generators.russian import RussianGenerator
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC


class GeneratorMenu(ScreenABC):

    def __init__(self, game_state: GameState, parent_screen: ScreenABC, screen: Surface):
        super().__init__(screen)

        self.__parent_screen = parent_screen

        self.__game_state = game_state

        self.__selected_generator = None

        generators = {
            "PythonGenerator": PythonGenerator,
            "CSharpGenerator": CSharpGenerator,
            "RussianGenerator": RussianGenerator,
            "EnglishGenerator": EnglishGenerator
        }

        for name, generator_cls in generators.items():
            self.add_button(Button((300, 70), name, action=lambda gen=generator_cls(): self.set_generator(gen)))

        self.add_button(Button((300, 70), 'Back', action=self.go_parent_screen))

    def go_parent_screen(self):
        self.__game_state.active_screen = self.__parent_screen

    def set_generator(self, generator):
        self.__selected_generator = generator
        self.change_text_generator()

    def change_text_generator(self):
        if self.__selected_generator is not None:
            self.__game_state.generator = self.__selected_generator
            print(f"Выбран генератор: {type(self.__game_state.generator).__name__}")
