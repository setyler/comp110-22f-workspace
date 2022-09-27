"""More utils!"""
__author__ = "730494915"


def only_evens(list_of_ints: list[int]) -> list[int]:
    """Given a list of integers, returns only evens."""
    output_list: list[int] = []
    i: int = 0
    while int(len(list_of_ints)) > 0 and i < int(len(list_of_ints)):
        if int(list_of_ints[i]) % 2 == 0:
            output_list.append(int(list_of_ints[i]))
        i += 1
    return output_list 


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, adds them together. Output list consists of all of list one and then all of list two, in the input order."""
    output_list: list[int] = []
    i: int = 0 
    while i < int(len(list_1)) and int(len(list_1)) > 0:
        output_list.append(int(list_1[i]))
        i += 1
    i = 0
    while i < int(len(list_2)) and int(len(list_2)) > 0:
        output_list.append(int(list_2[i]))
        i += 1
    return output_list
# this funciton is just a hot mess according to the autograder 


def sub(list: list[int], start: int, end: int) -> list[int]:
    """Given a list and start and end indices, outputs subset list."""
    output_list: list[int] = []
    i: int = 0 
    if end <= start:
        return output_list 
    if start < 0:
        start = 0
    if end > int(len(list)):
        end = int(len(list)) - 1
    while i < start:
        i = start
    while i < end:
        output_list.append(int(list[i]))
        i += 1 
    return output_list