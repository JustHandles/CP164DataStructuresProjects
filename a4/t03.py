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
from functions import queue_split_alt
from Queue_array import Queue
# Constants
num = [5, 6, 7, 8]
source = Queue()
for x in range(len(num)):
    source.insert(num[x])
target1, target2 = queue_split_alt(source)
for v in target1:
    print(v)
print("list2")
for v in target2:
    print(v)
