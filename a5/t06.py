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
values = [1, 2, 3, 3, 5, 5, 6, 3, 6]
for x in range(len(values)):
    source.prepend(values[x])
value = source.remove_front()
print("value removed:", value)
value = source.remove_front()
print("value removed:", value)
for v in source:
    print(v)
