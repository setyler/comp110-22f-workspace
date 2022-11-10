"""11/10/22 class: "vectorized" operations via magic metjods."""

from __future__ import annotations 
from typing import Union 


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.item = items 

    def __repr__(self) -> str:
        return f"StrArray({self.item})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items: 
                result.items.append(item + rhs)
        else: 
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result 


a: StrArray = (["Armando", "Pete", "Leaky"])
b: StrArray = (["Bacot", "Nance", "Black"])
print(a + "!")
print(a + b)