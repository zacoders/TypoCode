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


def test_rhythm_with_long_delay():
    time_provider = TimeProvider()
    calc = LineStatsCalc(time_provider)
    intervals = [1.0, 1.0, 1.0, 30.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    rhythm_percentage = calc.get_rhythm(intervals)
    print(f'{rhythm_percentage=}')
    assert rhythm_percentage > 33 and rhythm_percentage < 34


def test_rhythm_real_life():
    time_provider = TimeProvider()
    calc = LineStatsCalc(time_provider)
    intervals = [
        0.444680, 0.409908, 0.477721, 0.448560, 0.426258, 0.446133, 0.431645, 0.432888,
        0.409544, 0.457144, 0.397899, 0.511224, 0.411902, 0.439939, 0.411013, 0.380297,
        0.524795, 0.430236, 0.417535, 0.398490, 0.428456, 0.428049, 0.444058, 0.556887,
        0.479210, 0.414027, 0.429329, 0.393426, 0.411811, 0.443161, 0.400305, 0.411845,
        0.414705, 0.427810, 0.377411, 0.427461, 0.428311, 0.427365
    ]
    rhythm_percentage = calc.get_rhythm(intervals)
    assert rhythm_percentage > 94 and rhythm_percentage < 95
