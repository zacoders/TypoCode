
from generators.base import BaseGenerator
from generators.python import PythonGenerator
from ui.menus.basic.button_manager import ButtonManager


class GameState:
    def __init__(self):
        self.is_started: bool = False
        self.generator: BaseGenerator = PythonGenerator()
