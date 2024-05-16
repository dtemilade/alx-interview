#!/usr/bin/python3
''' Script for The N queens puzzle.
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
    Returns:
        the input in int type. Exceptions are defined accordingly.
    '''
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    '''Method for two queens are in an attacking mode.
    Args:
        pos1 contains the first queen's position.
        pos2 contains the second queen's position.
    Returns:
        True for queens are in an attacking position otherwise False.
    '''
    if (pos1[0] == pos2[0]) or (pos1[1] == pos2[1]):
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def group_checking(group):
    '''Checks if a group exists in the list of return values.
    Args:
        Group are possible positions.
    Returns:
        True if it exists otherwise False.
    '''
    global retval
    for chars in retval:
        i = 0
        for chars_pos in chars:
            for grp_pos in group:
                if chars_pos[0] == grp_pos[0] and chars_pos[1] == grp_pos[1]:
                    i = i + 1
        if i == n:
            return True
    return False


def build_val(row, group):
    '''Method for posible solution for the n queens
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    '''
    global retval
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_checking(tmp0):
            retval.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_val(row + 1, group)
            group.pop(len(group) - 1)


def get_retval():
    '''Method for final solution for the given chessboard size.
    '''
    global pos, n
    pos = [[i // n, i % n] for i in range(n ** 2)]
    a = 0
    group = []
    build_val(a, group)


n = get_input()
get_retval()
for val in retval:
    print(val)
