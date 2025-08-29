"""
-------------------------------------------------------
[Task 1 , Assignment 2]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin
from Food_utilities import read_foods
# Constants
filename = "foods.txt"
file_variable = open(filename, 'r')
foods = read_foods(file_variable)
origin = 7
print(f'Origin number: {origin}')
o_foods = by_origin(foods, origin)
file_variable.close()


for f in o_foods:
    print(f)
    print()
