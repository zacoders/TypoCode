
from collections import defaultdict
from typing import List, Tuple


class CharStats:
    def __init__(self):
        self.__stats = defaultdict(lambda: {'total_time': 0.0, 'count': 0})

    def update_stats(self, char: str, time_taken: float):
        self.__stats[char]['total_time'] += time_taken
        self.__stats[char]['count'] += 1

    def get_top_n_chars_by_avg_time(self, n: int) -> List[str]:
        # Compute average time for each character
        avg_times = [
            (char, data['total_time'] / data['count'])
            for char, data in self.__stats.items()
            if data['count'] > 0
        ]
        # Sort by average time in descending order and take top n characters
        avg_times.sort(key=lambda x: x[1], reverse=True)
        return [char for char, _ in avg_times[:n]]
