"""LS28: Recursion"""

from __future__ import annotations 
from typing import Union 

class Node: 
    data: int 
    next: Union[Node, None] 

    def __init__(self, data: int, next: Union[Node, None]):
        self.data = data
        self.next = next 
    
    def __str__(self) -> str:
        """Recursive method call."""
        if self.next == None:
            return f"{self.data} -> None" 
        else:
            return f"{self.data} -> {self.next}"


def sum(node: Node) -> int:
    """Recursive function.""" 
    if node.next == None:
        return node.data 
    else: 
        return node.data + sum(node.next)


def count(node: Node, current_count: int = 0) -> int:
    """return number of nodes in linked list """
    if node.next == None:
        return current_count + 1 
    else: 
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head) 

print(sum(head))
print(count(head))
print(head)