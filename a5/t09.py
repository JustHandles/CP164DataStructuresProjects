"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants
source = List()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(len(values)):
    source.append(values[x])
target1, target2 = source.split_alt()
print("first Half")
for v in target1:
    print(v)
print("second half")
for v in target2:
    print(v)
