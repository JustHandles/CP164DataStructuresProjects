"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
source1 = Stack()
source1_vals = [12, 14, 11, 10, 4]

for x in range(len(source1_vals)):
    source1.push(source1_vals[x])
print("source1")
for v in source1:
    print(v)
    print()
source1.reverse()
print("reverse")
for v in source1:
    print(v)
    print()
# Constants
