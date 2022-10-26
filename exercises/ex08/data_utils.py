"""Dictionary related utility functions."""

__author__ = "730496915"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows in a csv into table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")  # read file
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()  # close file 
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]  
        result.append(item)  
    return result 


def columnar(input: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table represented as a list of rows into one represented by a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = input[0]
    for column in first_row: 
        result[column] = column_values(input, column)
    return result 


def head(input_columns: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns column oriented data with only the specified number of columns."""
    output_data: dict[str, list[str]] = {}
    for key in input_columns:  # loops through the name of each column
        column_values: list[str] = []  # list for first N values
        i: int = 0 
        while i < n: 
            column_values.append(input_columns[key][i])
            i += 1 
        output_data[key] = column_values 
    return output_data 


def select(input_columns: dict[str, list[str]], new_columns: list[str]) -> dict[str, list[str]]:
    """Produces a column-based table with only a specific subset of the original columns."""
    output_columns: dict[str, list[str]] = {}
    for value in new_columns:
        output_columns[value] = input_columns[value]
    return output_columns


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column oriented data sets."""
    output_dict: dict[str, list[str]] = {}
    for value in dict_1:
        output_dict[value] = dict_1[value]
    for value in dict_2:
        if value in output_dict:
            output_dict[value] += dict_2[value]
        else:
            output_dict[value] = dict_2[value]
    return output_dict 


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