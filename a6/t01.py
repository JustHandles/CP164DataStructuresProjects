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
from Queue_linked import Queue

# Constants
queue = Queue()
b = queue.is_empty()
print("is empty? ", b)
n = len(queue)
print("length of queue: ", n)
value = 10
queue.insert(value)
queue.insert(value)
for v in queue:
    print("value: ", v)
value = queue.remove()
print("value removed: ", value)
value = queue.peek()
print("front of queue: ", value)
