"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-04-22"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
from List_linked import List
# Constants
lst = Sorted_List()
lst1 = List()
lst2 = List()
for x in range(10):
    lst1.append(x)
    lst2.append(x)
lst.intersection(lst1, lst2)
for x in lst:
    print(x)
