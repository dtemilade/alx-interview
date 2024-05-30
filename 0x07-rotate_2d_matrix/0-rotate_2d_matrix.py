#!/usr/bin/python3
'''0. Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''Method to rotate 90 degrees clockwise.
    '''
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    mat_row = len(matrix)
    mat_col = len(matrix[0])
    if not all(map(lambda x: len(x) == mat_col, matrix)):
        return
    c, r = 0, mat_row - 1
    for i in range(mat_col * mat_row):
        if i % mat_row == 0:
            matrix.append([])
        if r == -1:
            r = mat_row - 1
            c = c + 1
        matrix[-1].append(matrix[r][c])
        if c == mat_col - 1 and r >= -1:
            matrix.pop(r)
        r = r - 1
