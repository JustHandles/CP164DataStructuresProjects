"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-22"
-------------------------------------------------------
"""
from BST_linked import BST
import random
bst = BST()
for x in range(10):
    value = random.randint(0, 25)
    b = bst.insert(value)
for v in bst:
    print(v)
zero, one, two = bst.node_counts()
print(zero, one, two)
key = int(input("Enter a node value to find the parent of"))
value = bst.parent(key)
print(value)
