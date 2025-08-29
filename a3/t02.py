"""
-------------------------------------------------------
[Task , Lab]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
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
source2 = Stack()
source2_vals = [16, 5, 9, 2, 6, 21, 10, 8]

for x in range(len(source2_vals)):
    source2.push(source2_vals[x])
print("source2")
for v in source2:
    print(v)
    print()
target = Stack()
target.combine(source1, source2)
print()
print("combined")
for v in target:
    print(v)
