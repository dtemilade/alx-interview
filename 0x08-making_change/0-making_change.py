#!/usr/bin/python3
'''0x08-making_change Project
'''


def makeChange(coins, total):
    '''Change comes from within
    '''
    if total <= 0:
        return 0
    count_coins = 0
    indexes = 0
    sorted_coins = sorted(coins, reverse=True)
    k = len(coins)
    while total > 0:
        if indexes >= k:
            return -1
        if total - sorted_coins[indexes] >= 0:
            total -= sorted_coins[indexes]
            count_coins += 1
        else:
            indexes += 1
    return count_coins
