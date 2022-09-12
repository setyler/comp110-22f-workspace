"""Recreating common functions for lists."""
__author__ = "730496915"


def all(input_list: list[int], input_int: int) -> bool:
    """Given a list of integers and a single integers, determines whether all integers in list equal single integer."""
    i: int = 0 
    result = False
    if len(input_list) == 0:
        return result
    while i < len(input_list) or not result:
        if input_list[i] == input_int:
            result = True 
            i += 1
        else:
            result = False 
            return result
    return result 


def max(input: list[int]) -> int:
    """Given a list of integers, returns the largest."""
    i: int = 0
    result: int = 0
    if len(input) == 0: 
        raise ValueError("max() is an empty List")
    if len(input) == 1:
        result = input[0]
        return result
    else:
        result = input[0]
        while i < len(input):
            if input[i] > result:
                result = input[i]
            i += 1 
    return result 


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Given two lists of integers, determines whether each item in each list is equal to one another."""
    result: bool = False
    i: int = 0
    if len(input_1) != len(input_2): 
        return result 
    if len(input_1) == 0 and len(input_2) == 0:
        result = True 
        return result
    while i < len(input_1): 
        if input_1[i] == input_2[i]:
            result = True 
            i += 1 
        else: 
            result = False 
            return result
    return result 