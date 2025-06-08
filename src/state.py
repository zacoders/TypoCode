
import pygame
from generators.generator_abc import GeneratorABC
from common.sound_enum import SoundEnum


class State:
    def __init__(self):
        self.generator: GeneratorABC
        self.is_help_showed: bool = False
        self.sound_state: SoundEnum = SoundEnum.ON
