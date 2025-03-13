from pygame import Surface
import inspect
import generators
from generators.base import BaseGenerator
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC


class GeneratorMenu(ScreenABC):

    def __init__(self, game_state: GameState, parent_screen: ScreenABC, screen: Surface):
        super().__init__(screen)

        self.__parent_screen = parent_screen

        self.__game_state = game_state

        self.__buttons_size = (300, 70)

        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, BaseGenerator):
                self.add_button(
                    Button(self.__buttons_size, name, action=lambda gen=generator_cls(): self.set_generator(gen))
                )

    def set_generator(self, generator):
        self.__game_state.generator = generator
        print(f"Выбран генератор: {type(self.__game_state.generator).__name__}")
        self.__game_state.active_screen = self.__parent_screen
