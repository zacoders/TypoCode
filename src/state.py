
from generators.generator_abc import GeneratorABC


class State:
    def __init__(self):
        self.generator: GeneratorABC
        self.is_help_showed: bool = False
