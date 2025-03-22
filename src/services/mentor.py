
from services.line_stats import LineStats


class Mentor:

    def __init__(self):
        self.__typing_level = 0

    @property
    def typing_level(self) -> int: return self.__typing_level

    def update_stats(self, stats: LineStats):

        if self.__typing_level >= 5:
            return

        self.__typing_level += 1
