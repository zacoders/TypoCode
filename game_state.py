
from generators.base import BaseGenerator
from generators.python import PythonGenerator


class GameState:
    def __init__(self):
        self.is_started: bool = False
        self.generator: BaseGenerator = PythonGenerator()
