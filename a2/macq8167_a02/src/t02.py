"""
-------------------------------------------------------
[Task 2 , Assignment 2]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories
from Food_utilities import read_foods
# Constants
filename = "foods.txt"
file_variable = open(filename, 'r')
foods = read_foods(file_variable)
avg = average_calories(foods)
file_variable.close()
print(f'Expected value: 791.44, Calculated value: {avg:.2f}')
