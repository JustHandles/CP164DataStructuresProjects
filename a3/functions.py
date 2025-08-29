"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Justin MacQueen
ID:      169058167
Email:   macq8167@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
OPERATORS = "+-*/"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    hold_deez = []
    while not source.is_empty():
        hold_deez.append(source.pop())
    for x in range(len(hold_deez)):
        source.push(hold_deez[x])
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    stack1 = Stack()
    rev = []
    for x in range(len(string)):
        if string[x].isalpha():
            stack1.push(string[x].lower())
            rev.append(string[x].lower())
    for v in stack1:
        print(v)
    n = 0
    while not stack1.is_empty():
        val1 = stack1.pop()
        if val1 != rev[n]:
            palindrome = False
        n += 1
    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    answer = string
    stack = Stack()
    string = string.split(" ")
    for n in string:
        if n not in OPERATORS:
            stack.push(n)
        else:
            if not stack.is_empty():
                val1 = float(stack.pop())
            if not stack.is_empty():
                val2 = float(stack.pop())
            if n == "+":
                stack.push(val1+val2)
            elif n == "-":
                stack.push(val2-val1)
            elif n == "*":
                stack.push(val2*val1)
            elif n == "/":
                stack.push(val2/val1)
    if not stack.is_empty():
        answer = stack.pop()

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    n = 0
    key = 'Start'
    stack = Stack()
    values = maze[key]
    path = []
    for x in range(len(values)):
        stack.push(values[x])
    if not stack.is_empty():
        key = stack.pop()
        path.append(key)
    while key != 'X' and n != 1:
        values = maze[key]
        for x in range(len(values)):
            stack.push(values[x])
        if not stack.is_empty():
            if 'X' in values:
                key = 'X'
                path.append(key)
            else:
                key = stack.pop()
                path.append(key)
        elif stack.is_empty():
            n = 1
    return path
