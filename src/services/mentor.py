
from services.line_stats import LineStats


class Mentor:

    def __init__(self):
        self.__typing_level = 0

    @property
    def typing_level(self) -> int: return self.__typing_level

    def update_stats(self, stats: LineStats):

        if stats.error_count > 3:
            return

        if self.__typing_level >= 5:
            self.__typing_level = 5
            return

        if self.__typing_level == 0:
            if stats.speed_symbols_per_minute < 100:
                return
            if stats.speed_symbols_per_minute < 150:
                self.__typing_level += 1
                return
            self.__typing_level += 2
        else:
            if stats.speed_symbols_per_minute >= 100:
                self.__typing_level += 1
