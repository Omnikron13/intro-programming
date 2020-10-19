# -*- coding: utf-8 -*-
"""
@author: Joey (100322897)
"""

from math import sqrt


def linear(m, c):
    """
    Solves the equation y=mx+c for x where y=0 and m & c are arbitrary numbers.

    :param m: arbitrary non-zero number
    :param c: arbitrary number
    :return: x
    """
    return (0-c)/m


def quadSolver(a, b, c):
    """
    Solves quadratic equations with the quadratic formula.

    :param a: coefficient of x**2
    :param b: coefficient of x
    :param c: constant
    :return: list containing a pair of solutions, or None if it cannot be solved
    """
    n = b ** 2 - 4 * a * c
    if n < 0:
        print("Could not solve this equation.")
        return None
    x = [0,0]
    x[0] = (-b + sqrt(n)) / 2 * a
    x[1] = (-b - sqrt(n)) / 2 * a
    return x


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
