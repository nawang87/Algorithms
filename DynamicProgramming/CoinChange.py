def coinChange(coins, total):
    dp = [float('inf') for i in range(0, total+1)]
    dp[0]=0
    for sum in range(1, total+1):
        for value in coins:
            print(sum,value)
            if value<=sum and dp[sum-value]<dp[sum]:
                dp[sum]=dp[sum-value]+1
    print(dp)
    return dp[total]

coinChange([1,3,5], 10)
