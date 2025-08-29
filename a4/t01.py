"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
# Constants
target = Queue()
target.insert(5)
source = [5, 7, 9, 10]
target.remove()
target.remove()
for v in source:
    target.insert(v)
print(target.peek())
