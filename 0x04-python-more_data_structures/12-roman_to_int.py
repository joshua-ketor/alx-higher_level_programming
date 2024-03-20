#!/usr/bin/python3
def roman_to_int(roman_string):
    """convert a roman numeral to an integer"""
    # check if argument is a string
    if roman_string is None or not type(roman_string) is str:
        return 0

    # variables
    total = 0
    prev_value = 0
    roman_to_int = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # loop through each letter
    for letter in reversed(roman_string):
        value = roman_to_int.get(letter)
        if value is None:
            return 0

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total

    return total
