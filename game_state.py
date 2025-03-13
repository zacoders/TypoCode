
from generators.base import BaseGenerator
from generators.python import PythonGenerator
from ui.menus.basic.screen import ScreenABC
from dataclasses import dataclass


class GameState:
    def __init__(self):
        self.active_screen: ScreenABC | None = None
        self.generator: BaseGenerator = PythonGenerator()
