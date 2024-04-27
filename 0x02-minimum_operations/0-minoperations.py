#!/usr/bin/python3
'''method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
'''


def minOperations(n):
    '''method that calculates the fewest number of operations
    '''
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0
    var = 1
    count = 0
    dup = 0
    while var < n:
        if n % var != 0:
            var += dup
            count += 1
        else:
            dup = var
            var = var + dup
            count = count + 2
    return (count if var == n else 0)
