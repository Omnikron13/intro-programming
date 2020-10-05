# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:00:34 2020

@author: Joey (100322897)
"""


def get_int(msg):
    x = input(msg)
    try:
        return int(x)
    except ValueError:
        print("Error: not an integer")
        return get_int(msg)


def calculate(x, m, c):
    y = (m * x) + c
    print(f"Where x = {x}, y = {y}")


m = get_int("Please enter an integer: ")
c = get_int("Please enter another integer: ")


for x in range(1, 11):
    calculate(x, m, c)


calculate(get_int("Please enter a value for x: "), m, c)