"""Testing functions from utils (ex05)."""
__author__ = "730496915"

from utils import only_evens, concat, sub 


# only_evens tests: 


def test_only_evens_empty() -> None:
    """Tests output for an empty input list."""
    list_of_ints: list[int] = []
    assert only_evens(list_of_ints) == []


def test_only_evens_mix() -> None:
    """Tests output for input list without multiple odds and evens."""
    list_of_ints: list[int] = [1, 2, 3, 6]
    assert only_evens(list_of_ints) == [2, 6]


def test_only_evens_negatives() -> None:
    """Tests output for input list including positive and negative integers."""
    list_of_ints: list[int] = [-5, -4, 1, 4, 5]
    assert only_evens(list_of_ints) == [-4, 4]


# concat tests:


def test_concat_empty() -> None:
    """Tests output list given empty input lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_different_lengths() -> None:
    """Tests output for lists of different lengths."""
    list_1: list[int] = [1, 2, 80, -8]
    list_2: list[int] = [0]
    assert concat(list_1, list_2) == [1, 2, 80, -8, 0]


def test_concat_same_list() -> None:
    """Tests output for two equal input lists."""
    list_1: list[int] = [1, 5, -2]
    list_2: list[int] = [1, 5, -2]
    assert concat(list_1, list_2) == [1, 5, -2, 1, 5, -2]


# sub tests:


def test_sub_empty() -> None: 
    """Given an empty list, test output."""
    list: list[int] = []
    start_index: int = 0
    end_index: int = 0
    assert sub(list, start_index, end_index) == []


def test_sub_change_indeces() -> None: 
    """Given indexes that do not exist in the list, test for change."""
    list: list[int] = [0, 1, 2, 3, 4, 5]
    start_index: int = -2
    end_index: int = 8
    assert sub(list, start_index, end_index) == [0, 1, 2, 3, 4, 5]


def test_sub_no_change() -> None:
    """Given the current start and end indices, tests for change (or lack thereof)."""
    list: list[int] = [0, 1, 2, 3]
    start_index: int = 0
    end_index: int = 3
    assert sub(list, start_index, end_index) == list 


def test_sub_random_case() -> None:
    """Given a random typical case."""
    list: list[int] = [-100, 85, 2, 16, 0, 94, 39, 3, 3]
    start_index: int = 2
    end_index: int = 5
    assert sub(list, start_index, end_index) == [2, 16, 0, 94]


