"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-31"
-------------------------------------------------------
"""
# Imports
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
values = [99, 82, 53, 78, 18, 72]
for x in values:
    a.append(x)

Sorts.radix_sort(a)
for x in a:
    print(x)
