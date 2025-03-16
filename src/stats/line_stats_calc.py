

from common.time_provider import TimeProvider
from stats.line_stats import LineStats


class LineStatsCalc:

    def __init__(self, time_provider: TimeProvider = TimeProvider()):
        self.__success_count = 0
        self.__time_provider = time_provider
        self.__start_time_utc = None
        self.__end_time_utc = None

    def symbol_typed(self, is_error: bool, max_len: int):

        if not self.__start_time_utc:
            self.__start_time_utc = self.__time_provider.get_utc_time()

        if is_error:
            self.__error_count += 1
        else:
            self.__success_count += 1

        if self.__success_count == max_len:
            self.__end_time_utc = self.__time_provider.get_utc_time()

    def get_stats(self) -> LineStats:
        end_time = self.__end_time_utc if self.__end_time_utc else self.__time_provider.get_utc_time()
        start_time = self.__start_time_utc if self.__start_time_utc else end_time
        duration_minutes: float = (end_time - start_time).total_seconds() / 60.0
        if duration_minutes == 0:
            speed_symbols_per_minute = 0
        else:
            speed_symbols_per_minute: float = self.__success_count / duration_minutes
        return LineStats(error_count=self.__error_count, speed_symbols_per_minute=speed_symbols_per_minute)
