"""More utils!"""
__author__ = "730494915"


def only_evens(list_of_ints: list[int]) -> list[int]:
    """Given a list of integers, returns only evens."""
    output_list: list[int] = []
    i: int = 0
    while len(list_of_ints) > 0 and i < len(list_of_ints):
        if list_of_ints[i] % 2 == 0:
            output_list.append(int(list_of_ints[i]))
        i += 1
    return output_list 


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, adds them together. Output list consists of all of list one and then all of list two, in the input order."""
    output_list: list[int] = []
    i: int = 0 
    while i < len(list_1):
        output_list.append(int(list_1[i]))
        i += 0
    i = 0
    while i < len(list_2):
        output_list.append(int(list_2[i]))
        i += 1
    return output_list
# this funciton is just a hot mess according to the autograder 

def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list and two indexes, produces a list of only the values between the specified ideces."""
    output_list: list[int] = []
    if end_index <= start_index:
        return output_list
    i: int = 0
    if start_index < 0:
        start_index = 0 
    if end_index >= len(list):
        end_index = len(list) - 1
    while i < start_index:
        i += 1
    while i <= end_index:
        output_list.append(int(list[i]))
        i += 1
    return output_list