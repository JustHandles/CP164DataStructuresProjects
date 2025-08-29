"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants
deque = Deque()
values = [1, 2, 3, 4, 5, 6, 7]
for v in values:
    deque.insert_front(v)
v = deque.remove_rear()
print("value removed:", v)
print("remaining values:")
for v in deque:
    print(v)
