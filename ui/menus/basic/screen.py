from abc import ABC
from pygame import Surface
from pygame.event import Event
from typing import List
from ui.menus.basic.blur import Blur
from ui.menus.basic.button import Button


class ScreenABC(ABC):

    def __init__(self, screen: Surface):
        self.__screen = screen

        self.blur = Blur(self.__screen)
        self.buttons: list[Button] = []

    def add_button(self, button: Button):
        self.buttons.append(button)
        self.update_button_positions()

    def update_button_positions(self):
        buttons_count = len(self.buttons)
        for button_num in range(0, buttons_count):
            button_pos = (self.__screen.get_width() / 2, (self.__screen.get_height() / buttons_count / 2) +
                          (self.__screen.get_height() / buttons_count * button_num))
            self.buttons[button_num].set_position(button_pos)

    def update(self, events: List[Event]):
        for event in events:
            for button in self.buttons:
                button.update(event)

    def draw(self):
        if self:
            self.blur.draw()
            for button in self.buttons:
                button.draw(self.__screen)
