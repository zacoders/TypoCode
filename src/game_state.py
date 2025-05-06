
from generators.generator_abc import GeneratorABC


class GameState:
    def __init__(self):
        self.generator: GeneratorABC
        self.is_help_showed: bool = False
