#!/usr/bin/python3
'''
Script for The N queens puzzle.
'''
import sys


retval = []
'''Possible return values to the N queens problem.
'''
n = 0
'''Actual size of the chessboard.
'''
pos = None
'''Various positions on the chessboard.
'''


def get_input():
    '''Accepts and validates inputs from user.
    Returns the input in int type.
    Exceptions are defined accordingly.
    '''
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    '''Method to check if two queens are in an attacking mode.
    Args:
        pos1: The first queen's position.
        pos2: The second queen's position.
    Returns:
        True if queens are in an attacking position otherwise False.
    '''
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def group_checking(group):
    '''Checks if a group exists in the list of return values.
    Args:
        group: Possible positions.
    Returns:
        True if it exists otherwise False.
    '''
    global retval
    for solution in retval:
        if all(any(pos1 == pos2 for pos2 in solution) for pos1 in group):
            return True
    return False


def build_val(row, group):
    '''Finds possible solutions for the n queens problem.
    Args:
        row (int): The current row on the chessboard.
        group (list of lists): The group of valid positions.
    '''
    global retval, n
    if row == n:
        if not group_checking(group):
            retval.append(group.copy())
    else:
        for col in range(n):
            pos_index = row * n + col
            if all(not is_attacking(pos[pos_index], placed) for placed in group):
                group.append(pos[pos_index])
                build_val(row + 1, group)
                group.pop()


def get_retval():
    '''Finds the final solution for the given chessboard size.
    '''
    global pos, n
    pos = [[i // n, i % n] for i in range(n ** 2)]
    build_val(0, [])


n = get_input()
get_retval()
for solution in retval:
    print(solution)
