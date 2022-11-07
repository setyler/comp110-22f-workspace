"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


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

    def distance(self, point_2: Point) -> float:
        """Calculates the distance between 2 points."""
        distance: float = sqrt((self.x - point_2.x) * (self.x - point_2.x) + (self.y - point_2.y) * (self.y - point_2.y))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int

    def __init__(self, location: Point, direction: Point, sickness: int):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        self.sickness = sickness

    def tick(self) -> None: 
        """Updates object position and status."""
        self.location = self.location.add(self.direction) 
        if self.is_infected(): 
            self.sickness += 1 
        if self.sickness == constants.RECOVERY_PERIOD: 
            self.immunize() 

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "deep sky blue"
        elif self.is_vulnerable():
            return "gray"        
        else:
            return "red"
    
    def contract_disease(self):
        """Updates cell status to infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Tests cell status for vulnerability."""
        if self.sickness == constants.VULNERABLE:
            return True 
        else:
            return False 

    def is_infected(self) -> bool:
        """Tests cell status for infection."""
        if self.sickness >= constants.INFECTED: 
            return True 
        else:
            return False 

    def is_immune(self) -> bool:
        """Tests cell status for immunity."""
        if self.sickness == constants.IMMUNE:
            return True 
        else:
            return False 
    
    def contact_with(self, cell_1: Cell): 
        """Process for when cells come into contact with each other."""
        if self.is_vulnerable() and cell_1.is_infected():
            self.contract_disease()
        if self.is_infected() and cell_1.is_vulnerable():
            cell_1.contract_disease()
    
    def immunize(self):
        """Changes cell's sickness attribute to immune."""
        self.sickness = constants.IMMUNE 

    
class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    number_infected: int
    number_immune: int = 0 

    def __init__(self, cells: int, speed: float, starting_infected: int, number_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        self.number_infected = starting_infected
        self.number_immune = number_immune 
        if self.number_infected >= constants.CELL_COUNT or self.number_infected <= 0:
            raise ValueError(f"Number of infected cells must be less than {constants.CELL_COUNT} and greater than zero.")
        if self.number_immune >= constants.CELL_COUNT or self.number_immune < 0: 
            raise ValueError(f"Number of immune cells must be less than {constants.CELL_COUNT}.")
        if self.number_immune + self.number_infected > constants.CELL_COUNT:
            raise ValueError(f"Number of infected cells plus immune cells must be less than {constants.CELL_COUNT}.")
        for _ in range(cells): 
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            sickness: int = constants.VULNERABLE  
            if len(self.population) < self.number_infected:
                sickness = constants.INFECTED
            elif len(self.population) < self.number_immune + self.number_infected:
                sickness = constants 
            cell: Cell = Cell(start_location, start_direction, sickness)
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

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
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Tests whether two cells in the population make contact."""
        i: int = 0 
        while i < len(self.population):
            j: int = i + 1 
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1 
            i += 1 

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_vulnerable() or cell.is_immune():
                return True
        else:
            return False