#!/user/bin/python3
"""making change module
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf') for _ in range(total + 1)]
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] != float('inf') else -1


        






        





    

