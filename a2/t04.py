"""
-------------------------------------------------------
[Task 4 , Assignment 2]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from Food_utilities import food_table
from Food_utilities import read_foods
# Constants
filename = "foods.txt"
file_variable = open(filename, 'r')
foods = read_foods(file_variable)
copy = deepcopy(foods)
copy.sort()
food_table(copy)
file_variable.close()
