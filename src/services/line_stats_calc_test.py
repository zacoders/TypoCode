from common.time_provider import TimeProvider
from services.line_stats_calc import LineStatsCalc


def test_rhythm_100_percent():
    time_provider = TimeProvider()
    calc = LineStatsCalc(time_provider)
    intervals = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    rhythm_percentage = calc.get_rhythm(intervals)
    assert rhythm_percentage == 100


def test_rhythm_50_percent():
    time_provider = TimeProvider()
    calc = LineStatsCalc(time_provider)
    intervals = [1.0, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    rhythm_percentage = calc.get_rhythm(intervals)
    assert rhythm_percentage == 50
