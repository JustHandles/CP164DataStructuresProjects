"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-03-21"
-------------------------------------------------------
"""
# Imports
from Word import Word
# Constants
CAPACITY = 20


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    clean_words = []
    for line in fv:
        data = line.split(" ")
        for v in data:
            if v.isalpha():
                clean_words.append(v)
    for v in clean_words:
        target = Word(v.lower())
        hash_set.insert(target)
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    maxim = 0
    for word in hash_set:
        total += word.comparisons
        if word.comparisons > maxim:
            maxim = word.comparisons
            max_word = word
    return total, max_word
