"""
-------------------------------------------------------
[Task 1, assignment]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from functions import clean_list
# Constants

a = []
how_many = int(input("Number of values in list:  "))

for x in range(how_many):
    minuend_num = int(input("Enter value to be appended to list: "))
    a.append(minuend_num)
clean_list(a)
