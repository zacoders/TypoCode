
from typing import Any, Callable, Dict, List
from pygame import Surface
from pygame.event import Event
import pygame_gui

from ui.menus.basic.blur import Blur


class ButtonManager:

    def __init__(self, screen: Surface, manager: pygame_gui.UIManager,
                 buttons: Dict[pygame_gui.elements.UIButton, Callable[..., Any]]):

        self.__screen = screen
        self.__manager = manager
        self.__buttons = buttons

    def update(self, events: List[Event]):
        for event in events:
            if event.type != pygame_gui.UI_BUTTON_PRESSED:
                continue
            for button, action in self.__buttons.items():
                if event.ui_element == button:
                    action()

    def draw(self, screen: Surface):
        ...
