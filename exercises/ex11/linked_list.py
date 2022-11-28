"""Utility functions for working with Linked Lists."""

from __future__ import annotations 
from typing import Optional 

__author__ = "730496915"


class Node:
    """An item in a singly-linked list."""
    data: int 
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argumennt if tail."""
        self.data = data 
        self.next = next 
    
    def __str__(self) -> str: 
        """Produce a string visualization of the linked list."""
        if self.next is None: 
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True 
    elif lhs is None or rhs is None or lhs.data != rhs.data: 
        return False 
    else: 
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int: 
    """Returns the last value of a linked list, or raises a ValueError if the list is empty."""
    if head is None: 
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data 
    else: 
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns value at specified index."""
    if index < 0 or head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0: 
        return head.data 
    else: 
        index -= 1 
        return value_at(head.next, index)


def max(head: Optional[Node]) -> int:
    """Returns the max value in a linked list."""
    if head is None: 
        raise ValueError("Cannot call max with None") 
    elif head.next is None: 
        return head.data 
    else: 
        if head.data > max(head.data):
            return head.data 


def linkify(items: list[int]) -> Optional[Node]:
    """Returns linked list with values corresponding to input."""
    if items == []:
        return None 
    else: 
        output: Node = Node(items[0], None)
        items.pop(0)
        output.next = linkify(items)


def scale(head: Optional[Node], factor: Optional[int]) -> Optional[Node]:
    """Returns a new linked list where the datas are the product of the original and the factor."""
    if head is None: 
        return None 
    if factor is None:
        raise ValueError("Cannot call function without factor.")
    elif head.next is None: 
        output: Node = Node(head.data * factor, None)
        return output 
    else: 
        output: Node = Node(head.data * factor, scale(head.next))
        return output 


# none of my recursive functions are working except the most basic ones :(