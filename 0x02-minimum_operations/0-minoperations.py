#!/usr/bin/python3
'''method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
'''


def minOperations(n):
    '''method that calculates the fewest number of operations
    '''
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0
    nums = 1
    count = 0
    dup = 0
    while nums < n:
        if n % nums != 0:
            nums += dup
            count += 1
        else:
            dup = nums
            nums = nums + dup
            count = count + 2
    return (count if nums == n else 0)
