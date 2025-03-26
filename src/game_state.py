
from generators.generator_abc import GeneratorABC


class GameState:
    def __init__(self):
        self.is_started: bool = False
        self.generator: GeneratorABC
