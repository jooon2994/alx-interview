#!/user/bin/python3
"""making change module
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if coin > total:
            continue
        num_coins += total // coin
        total = total % coin
        if total == 0:
            return num_coins

    return -1

