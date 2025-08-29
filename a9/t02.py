"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-22"
-------------------------------------------------------
"""
# Imports
from functions import insert_words
from functions import comparison_total
from Hash_Set_sorted import Hash_Set
# Constants
q = Hash_Set(20)
filename = "otoos610.txt"
file_variable = open(filename, "r")
insert_words(file_variable, q)
file_variable.close()
total, max_word = comparison_total(q)
print("Using array-based list Hash_Set")
print()
print("Total Comparisons:", f'{total:,}')
print("Word with most comparisons,", f'"{max_word}"')
