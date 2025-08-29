"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants
lst = List()
for x in range(10):
    lst.append(99)
key = 9
lst.remove_many(key)
for x in lst:
    print(x)
