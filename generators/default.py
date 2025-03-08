

import random
import string
from generators.base import BaseGenerator


class RandomGenerator(BaseGenerator):

    def get(self, len: int) -> str:
        result = ''
        for _ in range(len):
            random_char = random.choice(string.ascii_lowercase)
            result += random_char

        return result
