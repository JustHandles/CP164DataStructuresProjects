"""
-------------------------------------------------------
[Task 3, Assignment 2]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import calories_by_origin
from Food_utilities import read_foods
# Constants
filename = "foods.txt"
file_variable = open(filename, 'r')
foods = read_foods(file_variable)
origin = 8
print(f'Origin number: {origin}')
avg = calories_by_origin(foods, origin)
file_variable.close()
print(f"{avg:.1f}")
