"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-04-21"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants
lst = List()
source1 = List()
source2 = List()
for x in range(10):
    source1.append(x)
for x in range(10):
    source2.append(x)
lst.combine(source1, source2)
for x in lst:
    print(x)
