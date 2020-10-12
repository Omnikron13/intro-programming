# -*- coding: utf-8 -*-
"""
Created on Mon Oct  12 18:13:37 2020

@author: Joey (100322897)
"""


# My student ID number as a list of digits
id = [1,0,0,3,2,2,8,9,7]


# Print vertical bars representing the digits of the ID
for y in range(0, 10):
    print(f"{y} ", end='')
    for x in id:
        if x > y:
            print("|", end='')
        elif x == y:
            print("X", end='')
        else:
            print(" ", end='')
        print(" ", end='')
    print(f" {y}", end='\n')
