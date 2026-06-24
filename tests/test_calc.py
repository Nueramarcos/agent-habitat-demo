from habitat.calc import (
    clamp,
    geometric_mean,
    harmonic_mean,
    is_palindrome,
    mean,
    median,
    mode,
    rms,
    stddev,
    sum_range,
    variance,
    weighted_mean,
    percentile,
)


def test_sum_range_basic():
    assert sum_range(1, 5) == 15


def test_sum_range_reversed():
    assert sum_range(5, 1) == 15


def test_is_palindrome_simple():
    assert is_palindrome("racecar")
    assert is_palindrome("Racecar")
    assert not is_palindrome("hello")


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(99, 0, 10) == 10


def test_clamp_inverted_bounds():
    assert clamp(5, 10, 0) == 5


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([10, 20]) == 15.0


def test_mean_empty():
    assert mean([]) == 0.0


def test_median_odd():
    assert median([3, 1, 2]) == 2.0


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty():
    assert median([]) == 0.0


def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2


def test_mode_another():
    assert mode([4, 4, 4, 1, 1]) == 4


def test_mode_empty():
    assert mode([]) is None


def test_variance():
    assert variance([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]) == 4.0


def test_variance_empty():
    assert variance([]) == 0.0


def test_stddev():
    assert stddev([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]) == 2.0


def test_stddev_empty():
    assert stddev([]) == 0.0


def test_geometric_mean():
    assert geometric_mean([1.0, 2.0, 4.0]) == 2.0


def test_geometric_mean_empty():
    assert geometric_mean([]) == 0.0


def test_harmonic_mean():
    assert harmonic_mean([1.0, 2.0, 4.0]) == 12.0 / 7.0


def test_harmonic_mean_empty():
    assert harmonic_mean([]) == 0.0


def test_rms():
    assert rms([1.0, 2.0, 2.0]) == (3.0 ** 0.5)


def test_rms_empty():
    assert rms([]) == 0.0


def test_weighted_mean():
    assert weighted_mean([1.0, 2.0, 3.0], [1.0, 1.0, 8.0]) == 2.7


def test_weighted_mean_empty():
    assert weighted_mean([], []) == 0.0


def test_percentile_p25():
    assert percentile([1.0, 2.0, 3.0, 4.0], 25.0) == 1.75


def test_percentile_empty():
    assert percentile([], 50.0) == 0.0