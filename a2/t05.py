"""
-------------------------------------------------------
[Task 5 , Assignment 2]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search
from Food_utilities import read_foods
# Constants
filename = "foods.txt"
file_variable = open(filename, 'r')
foods = read_foods(file_variable)
origin = int(input("origin(int from -1 to 12): "))
max_cals = int(input("max_cals: "))
is_veg = input("Vegetarian(Y/N): ")
results = food_search(foods, origin, max_cals, is_veg)
file_variable.close()
print("\n")

for f in results:
    print(f)
    print()
