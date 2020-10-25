# -*- coding: utf-8 -*-
"""
@author: Joey (100322897)
"""


def inputInt(msg, min=None, max=None):
    """
    Wraps the input() function, requiring the inout to be a valid integer, with optional bounds.

    :param msg: input prompt to display
    :param min: optional minimum value allowed
    :param max: optional maximum value allowed
    :return:
    """
    # Get raw input
    x = input(msg)

    try:
        # Attempt to convert input to an integer
        x = int(x)

        # If min is set, check if the input is too low
        if min is not None and x < min:
            print(f"Error: the number cannot be less than {min}")
            return inputInt(msg, min, max)

        # If max is set, check if the input is too high
        if max is not None and x > max:
            print(f"Error: the number cannot be more than {max}")
            return inputInt(msg, min, max)

        # Return the validated integer
        return x

    # Recurse if the user enters anything but an integer
    except ValueError:
        print("Error: not an integer")
        return inputInt(msg, min, max)


def inputFloat(msg):
    """
    Wraps input() but insists on a valid float being entered.

    :param msg: input prompt to display
    :return: inputted valid float
    """
    # Get raw input from the user
    x = input(msg)

    # Return a float if a valid float was entered, otherwise recurse
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
    # Get a valid float from the user
    x = inputFloat(msg)

    # Return it if it isn't zero
    if x != 0:
        return x

    # Error and recurse if it is zero
    print("Error: this value may not be 0")
    return inputNonZeroFloat(msg)


def bubble(list):
    """
    Bubble sorts a given list.

    :param list: list to sort, expected to consist of numbers
    """
    # Flag for if any pairs have been swapped
    swapped = False

    # Check each pair of numbers in the list, swapping them if the first item is higher
    for n in range(len(list)-1):
        if list[n] > list[n+1]:
            list[n], list[n+1] = list[n+1], list[n]
            swapped = True

    # Recurse if any swaps have been performed
    if swapped:
        bubble(list)


def calculateY(x, m, c):
    """
    Calculates y - mx + c

    :param x: integer
    :param m: integer
    :param c: integer
    :return: None
    """
    y = (m * x) + c
    print(f"Where x = {x}, y = {y}")


def testLab1():
    """
    Runs tasks 1-7 from labsheet 1.

    :return: None
    """
    m = inputInt("Please enter an integer: ")
    c = inputInt("Please enter another integer: ")

    for x in range(1, 11):
        calculateY(x, m, c)

    calculateY(inputInt("Please enter a value for x: "), m, c)


def chartList(id):
    """
    Print a text-based bar chart of a list of digits.

    :param id: list of integers from 0-9
    :return: None
    """
    # Print a header
    print("| 0 1 2 3 4 5 6 7 8 9")

    # Print bars indicating each number in the ID
    for x in id:
        print("|-" + "--" * x + "X")

    # Print a footer
    print("| 0 1 2 3 4 5 6 7 8 9")


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
    # Calculate discriminant
    d = b ** 2 - 4 * a * c

    # Check if equation has real solutions
    if d < 0:
        print("Could not solve this equation.")
        return None

    # Initialise return list
    x = [0,0]

    # Calculate both possible solutions
    x[0] = (-b + sqrt(d)) / 2 * a
    x[1] = (-b - sqrt(d)) / 2 * a

    return x


def getUser(n):
    """
    Get a list of integers between 0 and 100 from the user.

    :param n: number of integers to get
    :return: list of the entered integers
    """
    # Initialise return list
    list = []

    # Get n integers 0-100 from the user
    for x in range(n):
        list.append(inputInt("Please enter an integer between 0 and 100: ", 0, 100))

    return list


def getAv(list):
    """
    Get the mean and median averages of a list of numbers.

    :param list: list to calculate averages for
    :return: list containing mean (index 0) and median (index 1) of the list
    """
    # First sort the list, as it needs to be sorted to get the median
    bubble(list)

    # Calculate the mean
    total = 0
    for n in list:
        total += n
    mean = total/len(list)

    # ...and the median
    if len(list) % 2:
        return [mean, list[len(list)//2]]
    mid = len(list)//2
    return [mean, (list[mid]+list[mid-1])/2]


def slicer(list):
    """
    Return the odd numbered elements or a reversed version of a list, depending on the mean & median values of the list.

    :param list: list to process
    :return: odd numbered elements if median >= mean, otherwise reversed version of the list
    """
    # Get the mean & median of the list
    avgs = getAv(list.copy())

    # Return odd numbered indexes if the median >= the mean
    if avgs[1] >= avgs[0]:
        return list[1::2]

    # ...else return a reversed version of the list
    return list[::-1]
