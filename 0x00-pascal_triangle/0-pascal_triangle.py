#!/usr/bin/python3
"""Creates a function that returns integers representing Pascal's Triangle"""


def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1's
        for j in range(1, i):  # Exclude the first and last elements
            try:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Calculate each element based on the row above
            except IndexError:
                pass  # If the index is out of bounds, it means the element is 1 (on the edge of the triangle)
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

def pascal_triangle(n):
    triangle = generate_pascals_triangle(n)
    return triangle

if __name__ == "__main__":
    pascal_triangle = pascal_triangle(5)
    print_pascals_triangle(pascal_triangle)
