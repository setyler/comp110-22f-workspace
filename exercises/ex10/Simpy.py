"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730496915"


class Simpy:
    values: list[float]

    def __init__(self, numbers: list[float] = []): 
        """Simpy constructor."""
        self.values = numbers

    def __repr__(self) -> str: 
        """String representation of Simpy class."""
        return f"Simpy({self.values})"

    def fill(self, filler: float, total: int):
        """Fills Simpy with given value."""
        if total > len(self.values):
            i: int = 0
            while i < len(self.values):
                self.values.append(filler)
                i += 1 

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills simpy with stepping range of values."""
        assert step != 0.0 
        self.values.append(start)
        while self.values[len(self.values) - 1] < stop - step: 
            self.values.append(self.values[len(self.values) - 1] + step)
    
    def sum(self) -> float: 
        """Adds all values of self together."""
        output: float = 0 
        for value in self.values: 
            output += value
        return output 

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds either float or corresponding values to Simpy object."""
        output: Simpy = Simpy()
        if isinstance(rhs, float):
            for value in self.values: 
                output.values.append(value + rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                output.values.append(self.values[i] + rhs.values[i])
        return output 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Raises all the values in given object to another given value."""
        output: Simpy = Simpy()
        if isinstance(rhs, float):
            for value in self.values: 
                output.values.append(value ** rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                output.values.append(self.values[i] ** rhs.values[i])
        return output         