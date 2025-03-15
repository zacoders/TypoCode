
from generators.base import GeneratorABC
from generators.c_sharp import CSharpGenerator


class GameState:
    def __init__(self):
        self.is_started: bool = False
        self.generator: GeneratorABC = CSharpGenerator()
