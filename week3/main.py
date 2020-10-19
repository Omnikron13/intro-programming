# -*- coding: utf-8 -*-
"""
@author: Joey (100322897)
"""


def linear(m, c):
    """
    Solves the equation y=mx+c for x where y=0 and m & c are arbitrary numbers.

    :param m: arbitrary non-zero number
    :param c: arbitrary number
    :return: x
    """
    return (0-c)/m


def inputFloat(msg):
    """
    Wraps input() but insists on a valid float being entered.

    :param msg: input prompt to display
    :return: inputted valid float
    """
    x = input(msg)
    try:
        return float(x)
    except ValueError:
        print("Error: not a number")
        return inputFloat(msg)


def inputNonZeroFloat(msg):
    """
    Further wraps inputFloat() with the additional constraint that the float input must be non-zero.

    :param msg: input prompt to display
    :return: inputted valid non-zero float
    """
    x = inputFloat(msg)
    if x != 0: return x
    print("Error: this value may not be 0")
    return inputNonZeroFloat(msg)


def test_linear():
    """
    Test the linear() function with user input
    """
    m = inputNonZeroFloat("Please enter a value for m: ")
    c = inputFloat("Please enter a value for c: ")
    print(f"x = {linear(m, c)}")


if __name__ == "__main__":
    test_linear()
