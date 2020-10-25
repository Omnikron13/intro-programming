# -*- coding: utf-8 -*-
"""
@author: Joey (100322897)
"""

def bubble(list):
    """
    Bubble sorts a given list.

    :param list: list to sort
    """
    swapped = False
    for n in range(len(list)-1):
        if list[n] > list[n+1]:
            list[n], list[n+1] = list[n+1], list[n]
            swapped = True
    if swapped:
        bubble(list)


def inputInt(msg, min=None, max=None):
    """
    Wraps the input() function, requiring the inout to be a valid integer, with optional bounds.

    :param msg: input prompt to display
    :param min: optional minimum value allowed
    :param max: optional maximum value allowed
    :return:
    """
    x = input(msg)
    try:
        x = int(x)
        if min is not None and x < min:
            print(f"Error: the number cannot be less than {min}")
            return inputInt(msg, min, max)
        if max is not None and x > max:
            print(f"Error: the number cannot be more than {max}")
            return inputInt(msg, min, max)
        return x
    except ValueError:
        print("Error: not an integer")
        return inputInt(msg, min, max)


def getUser(n):
    """
    Get a list of integers between 0 and 100 from the user.

    :param n: number of integers to get
    :return: list of the entered integers
    """
    list = []
    for x in range(n):
        list.append(inputInt("Please enter an integer between 0 and 100: ", 0, 100))
    return list


def getAv(list):
    """
    Get the mean and median averages of a list of numbers.

    :param list: list to calculate averages for
    :return: list containing mean (index 0) and median (index 1) of the list
    """
    bubble(list)
    total = 0
    for n in list:
        total += n
    mean = total/len(list)
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
    avgs = getAv(list.copy())
    if avgs[1] >= avgs[0]:
        return list[1::2]
    return list[::-1]
