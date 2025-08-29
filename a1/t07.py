"""
-------------------------------------------------------
[Task 7 , assignment 1]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from functions import max_diff
# Constants

a = []
how_many = int(input("Number of values in list: "))
for x in range(how_many):
    num = int(input("Enter value to add to list: "))
    a.append(num)
md = max_diff(a)
print(md)
