"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-17"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import fill_bst, letter_table, do_comparisons, comparison_total
# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

bst = BST()

fill_bst(bst, DATA1)

file_variable = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(file_variable, bst)
t2 = comparison_total(bst)

letter_table(bst)
