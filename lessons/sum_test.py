"""Tests for the sum function."""

from lessons.sum import sum

def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0

# pytest not working for me so this is where video following ends