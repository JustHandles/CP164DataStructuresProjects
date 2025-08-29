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
source1 = List()
source2 = List()
target = List()
values = [1, 2, 3, 3, 5, 5, 6, 3, 6]
for x in range(len(values)):
    source1.append(values[0])
    source2.append(values[x])
target.intersection(source1, source2)
for v in target:
    print(v)
