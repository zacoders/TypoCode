

from dataclasses import dataclass


@dataclass
class LineStats:
    error_count: int
    speed_symbols_per_minute: float
