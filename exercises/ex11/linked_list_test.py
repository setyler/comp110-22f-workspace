"""Tests for linked list utils."""

import pytest 
from exercises.ex11.linked_list import Node, last, value_at, linkify, max, scale  

__author__ = "730496915"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3 


def test_value_at_empty() -> None:
    """Empty list raises index error"""
    with pytest.raises(IndexError):
        value_at(None, 2)


def test_value_at_non_empty() -> None:
    """Returns correspondingly indexed value."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_max_empty() -> None:
    """ValueError if given nothing."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Returns highest value in linked list."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30 


def test_linkify_empty() -> None:
    """Returns nothing."""
    assert linkify(None) == None 


def test_linkify_non_empty() -> None:
    """Linkify test not edge."""
    assert linkify([1, 2, 3]) == "1 -> 2 -> 3 -> None"


def test_scale_empty() -> None: 
    """Scale test for no input."""
    assert scale(None) == None 


def test_scale_non_empty() -> None: 
    """Tests scale not empty."""
    assert scale(linkify([1, 2, 3]), 2) == "2 -> 4 -> 6 -> None"


# python -m pytest exercises/ex11/linked_list_test.py