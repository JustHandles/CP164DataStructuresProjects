"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Sorted_List_array import Sorted_List
# constants
sorted_list = Sorted_List()
sorted_list.insert(Food("Canuck Burger", 0, False, 7500))
source = Food("Canuck Burger", 0, None, None)
s = str(source)
print(s)
value = sorted_list.find(source)
print(value)
value = sorted_list.remove(source)
print(value)
for v in sorted_list:
    print(v)
