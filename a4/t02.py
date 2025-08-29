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
from Queue_array import Queue
# Constants
source = Queue()
target = Queue()
put_me_in = [5, 6, 7, 8]
for x in range(len(put_me_in)):
    source.insert(put_me_in[x])
    target.insert(put_me_in[x])
equals = source == target
print(equals)
