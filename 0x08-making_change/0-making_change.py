def makeChange(coins, total):
    if total <= 0:
        return 0

    table = [float('inf')] * (total+1)
    table[0] = 0

    for coin in coins:
        for i in range(coin, total+1):
            table[i] = min(table[i], table[i-coin]+1)

    return table[total] if table[total] != float('inf') else -1

