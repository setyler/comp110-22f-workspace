"""Exerise 07: Working with Dictionaries."""
__author__ = "730496915"


# python -m tools.submission exercises/ex07


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, swaps the key and value and returns a new dictionary."""
    output_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in output_dict:
            raise KeyError("Your input dictionary contains multiple equal values.")
        output_dict[input_dict[key]] = input_dict  # something in here is off 
    return output_dict 
# this functions is simply incorrect 


def favorite_color(input_dict: dict[str, str]) -> str:
    """Given input dictionary of favorite colors, gives the color that appears most."""
    tested: list[str] = []
    values: dict[str, str] = {}
    output_str: str = ""
    highest: int = 0
    for key in input_dict:
        i: int = 0
        if input_dict[key] not in tested:
            while i < len(input_dict):
                if input_dict[key] == input_dict[i]:
                    values[input_dict[key]] += 1 
            tested.append[input_dict[key]]
    for key in values:
        if values[key] > highest:
            output_str = key
    return output_str


def count(input_list: list[str]) -> dict[str, int]:
    """Returns dictionary that counts the number of items in the list."""
    output_dict: dict[str, int] = {}
    for item in input_list:
        output_dict[item] += 1 
    return output_dict 