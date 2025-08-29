"""
-------------------------------------------------------
[Task 4 , assignment 1]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

filename = "adresses.txt"
fh = open(filename, "r")
ucount, lcount, dcount, wcount, rcount = file_analyze(fh)
print(f'{ucount},{lcount},{dcount},{wcount},{rcount}')
fh.close()
