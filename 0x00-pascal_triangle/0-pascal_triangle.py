#!/usr/bin/python3
"""Creates a function that returns integers representing Pascal's Triangle"""


def generate_pascals_triangle(n):
    """
    Print the triangle
    """    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            try:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            except IndexError:
                pass
        triangle.append(row)
    return triangle

def pascal_triangle(n):
    """
    Print the triangle
    """
    triangle = generate_pascals_triangle(n)
    return triangle

if __name__ == "__main__":
    pass
