"""Tests for ex07: dictionaries."""
__author__ = "730496915"


# to run tests: python -m pytest exercises/ex07 


from dictionary import invert
from dictionary import favorite_colors 
from dictionary import count
import pytest


def test_invert_none() -> None:
    dict_1: dict[str, str] = {}
    assert invert(dict_1) == {}


def test_invert_generic_use() -> None: 
    dict_1: dict[str, str] = {'first': '1', 'second': '2', 'third': '3'}
    assert invert(dict_1) == {'1': 'first', '2': 'second', '3': 'third'}


def test_invert_single_entry() -> None: 
    dict_1: dict[str, str] = {'a': 'b'}
    assert invert(dict_1) == {'b': 'a'} 


with pytest.raises(KeyError):
    dict_1 = {'first': '1', 'second': '1'}
    invert(dict_1)


def test_favorite_color_empty() -> None:
    input_dict: dict[str, str] = {}
    assert favorite_colors(input_dict) == ""


def test_favorite_color_all_one() -> None:
    input_dict: dict[str, str] = {"Kate": "red", "Liam": "red", "Sue": "red", "Roxanne": "red"}
    assert favorite_colors(input_dict) == "red"


def test_favorite_color_random() -> None:
    input_dict: dict[str, str] = {"Kate": "blue", "Liam": "red", "Sue": "lavendar", "Roxanne": "red"}
    assert favorite_colors(input_dict) == "red"

def test_count_empty() -> None:
    input_list: list[str] = ()
    assert count(input_list) == ""


def test_count_all_one() -> None:
    input_list: list[str] = ("1", "1", "1", "1")
    assert count(input_list) == {"1": 4}


def test_count_random() -> None:
    input_list: list[str] = ("hello", "50", "next", "hello")
    assert count(input_list) == {"hello": 2, "50": 1, "next": 1}