"""Exerise 07: Working with Dictionaries."""
__author__ = "730496915"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, swaps the key and value and returns a new dictionary."""
    output_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in output_dict:
            raise KeyError("Your input dictionary contains multiple equal values.")
        else:
            output_dict[input_dict[key]] = str(key) 
    return output_dict 


def favorite_color(input_dict: dict[str, str]) -> str:
    """Given input dictionary of favorite colors, returns the color that appears most."""
    values: dict[str, int] = {}
    output_str: str = ""
    highest: int = 0 
    if len(input_dict) == 0:
        return output_str
    for key in input_dict:
        if input_dict[key] not in values:
            values[input_dict[key]] = 0
        values[input_dict[key]] += 1 
    for key in values: 
        if values[key] > highest: 
            output_str = key 
            highest = values[key]
    return output_str 


def count(input_list: list[str]) -> dict[str, int]:
    """Returns dictionary that counts the number of items in the list."""
    output_dict: dict[str, int] = {}
    if len(input_list) == 0:
        return output_dict 
    for item in input_list:
        if item not in output_dict:
            output_dict[item] = 0 
        output_dict[item] += 1 
    return output_dict 