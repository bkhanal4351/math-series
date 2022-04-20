from math_series.series import fibonacci, lucas, sum_series


def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_luc_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_sum_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_two():
    actual = sum_series(4, 3, 1)
    expected = 9
    assert actual == expected



