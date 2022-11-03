"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730496915" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None: 
        """Reassigns object's location attribute the result of adding location to direction."""
        self.location = self.location.add(self.direction)
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"
    
    def contract_disease(self):
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True 
        else:
            return False 
    
    def color(self) -> str:
        output: str = ""
        if self.is_vulnerable == True:
            output = "gray"
            return output
        else:
            output = "blue"
            return output 


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    number_infected: int = 1

    # if number_infected >= population or number_infected <= 0:
    #     raise ValueError(f"Number of infected cells must be less than {population}.")

    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_location: Point = Point(0, 0)
            start_direction: Point = Point(0, 0)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        number_infected = constants.STARTING_INFECTED
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed 
        direction_y: float = sin(random_angle) * speed 
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X or cell.location.x < constants.MIN_X:
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y or cell.location.y < constants.MIN_Y:
            cell.direction.y *= 1.0


    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False