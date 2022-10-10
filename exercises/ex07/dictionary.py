"""Exerise 07: Working with Dictionaries."""
__author__ = "730496915"


# python -m tools.submission exercises/ex07


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, swaps the key and value and returns a new dictionary."""
    output_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in output_dict:
            raise KeyError("Your input dictionary contains multiple equal values.")
        else:
            output_dict[input_dict[key]] = key 
    return output_dict 


def favorite_color(input_dict: dict[str, str]) -> str:
    """Given input dictionary of favorite colors, gives the color that appears most."""
    values: dict[str, int] = {}
    output_str: str = ""
    highest: int = 0 
    if len(input_dict) == 0:
        return output_str
    for key in input_dict:
        values[key] += 1 
    for key in values:
        if values[key] > highest:
            highest = values[key]
            output_str = f"{key}"
    return output_str


def count(input_list: list[str]) -> dict[str, int]:
    """Returns dictionary that counts the number of items in the list."""
    output_dict: dict[str, int] = {}
    for item in input_list:
        output_dict[item] += 1 
    return output_dict 
# and lastly, this function is also simply incorrect :( 