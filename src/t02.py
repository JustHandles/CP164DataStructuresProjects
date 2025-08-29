"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from functions import list_subtract
# Constants
minuend = []
subtrahend = []
how_manym = int(input("Number of values in minuend: "))

for x in range(how_manym):
    minuend_num = int(input("Enter value to be appended to minuend: "))
    minuend.append(minuend_num)
how_manys = int(input("Number of values in subtrahend: "))
for x in range(how_manys):
    subtrahend_num = int(input("Enter value to be appended to subtrahend: "))
    subtrahend.append(subtrahend_num)
list_subtract(minuend, subtrahend)
print(minuend)
