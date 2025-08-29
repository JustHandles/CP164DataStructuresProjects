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
from Priority_Queue_array import Priority_Queue
# Constants
num = [5, 7, 6, 8, 9, 8, 1]
source = Priority_Queue()
for x in range(len(num)):
    source.insert(num[x])
key = 7
target1, target2 = source.split_key(key)
print("Target1:")
for v in target1:
    print(v)
print("Target2:")
for v in target2:
    print(v)
