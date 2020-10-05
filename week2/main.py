# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:31:30 2020

@author: Joey (100322897)
"""


# My student ID number as a list of digits
id = [1,0,0,3,2,2,8,9,7]

print("| 0 1 2 3 4 5 6 7 8 9")

while len(id) > 0:
    s = "|-"
    pH = id.pop(0)
    while pH > 0:
        s += "--"
        pH -= 1
    else:
        s += "X"
    print(s)

print("| 0 1 2 3 4 5 6 7 8 9")

