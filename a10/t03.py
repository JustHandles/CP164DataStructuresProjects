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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque
a = Deque()
values = [99, 82, 53, 78, 18, 72]
for x in values:
    a.insert_front(x)
Sorts.gnome_sort(a)
for j in a:
    print(j)
