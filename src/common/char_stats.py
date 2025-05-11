
from collections import defaultdict


class CharStats:
    def __init__(self):
        self.__stats = defaultdict(lambda: {'total_time': 0.0, 'count': 0})

    def update_stats(self, char: str, time_taken: float):
        self.__stats[char]['total_time'] += time_taken
        self.__stats[char]['count'] += 1
