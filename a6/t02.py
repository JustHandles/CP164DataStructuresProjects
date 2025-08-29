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
from Priority_Queue_linked import Priority_Queue
# Constants
pq1 = Priority_Queue()
values = [11, 22, 33, 44]
for v in values:
    pq1.insert(v)
key = 33
target1, target2 = pq1.split_key(key)
for v in target1:
    print(v)
