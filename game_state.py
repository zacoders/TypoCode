
from generators.base import BaseGenerator
from generators.python import PythonGenerator
from ui.menus.basic.screen import ScreenABC


class GameState:
    def __init__(self):
        self.active_screen: ScreenABC | None
        self.generator: BaseGenerator = PythonGenerator()
