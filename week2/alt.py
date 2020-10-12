# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:31:30 2020

@author: Joey (100322897)
"""


# My student ID number as a list of digits
id = [1,0,0,3,2,2,8,9,7]

# Print a header
print("| 0 1 2 3 4 5 6 7 8 9")

# Print bars indicating each number in the ID
for x in id:
    print("|-" + "--" * x + "X")

# Print a footer
print("| 0 1 2 3 4 5 6 7 8 9")

