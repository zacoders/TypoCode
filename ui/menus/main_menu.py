import sys
from pygame import Surface
from pygame.font import Font
from ui.menus.basic.button import Button
from game_state import GameState
from ui.menus.basic.screen import ScreenABC
from ui.menus.generator_menu import GeneratorMenu


class MainMenu(ScreenABC):

    def __init__(self, game_state: GameState, screen: Surface):
        super().__init__(screen)

        self.__game_state = game_state

        self.__screen = screen

        change_dict_text = 'Change_Language_Dictionary'

        font = Font("fonts/UbuntuMono-Regular.ttf", round(25))

        button_size_base = [300, 70]

        while True:
            if font.render(change_dict_text, False, (255, 255, 255)).get_width() + 20 > button_size_base[0]:
                button_size_base[0] += 1
            elif font.render(change_dict_text, False, (255, 255, 255)).get_height() > button_size_base[1]:
                button_size_base[1] += 1
            else:
                break

        self.__button_size = (button_size_base[0], button_size_base[1])

        self.add_button(Button(self.__button_size, 'Change_Language_Dictionary', action=self.generators_screen))
        self.add_button(Button(self.__button_size, 'Start', action=self.start))
        self.add_button(Button(self.__button_size, 'Exit', action=lambda: sys.exit()))

    def start(self):
        self.__game_state.active_screen = None

    def generators_screen(self):
        self.__game_state.active_screen = GeneratorMenu(self.__game_state, self, self.__screen)
