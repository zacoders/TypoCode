

import random
import string
import pygame

from pygame.event import Event
from pygame.font import Font


class TextGenerator:

    def get(self, len: int) -> str:
        result = ''
        for _ in range(len):
            random_char = random.choice(string.ascii_lowercase)
            result += random_char

        return result
