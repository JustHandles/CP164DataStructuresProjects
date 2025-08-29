"""
-------------------------------------------------------
[Task 8 , assignement ]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants

a = []
number_of_lists = int(input("Enter number of lists in a: "))
nums_per_list = int(input("Enter the number of numbers per list: "))
for x in range(number_of_lists):
    lists = []
    for i in range(nums_per_list):
        number_to_list = float(input("Enter list value: "))
        lists.append(number_to_list)
    a.append(lists)
small, large, total, average = matrix_stats(a)
print(f'({small}, {large}, {total}, {average})')
