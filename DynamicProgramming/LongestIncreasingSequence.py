def findlongestincreasingsequence(nums):
    dp = [0 for i in range(len(nums))]
    dp[0]=1
    for i in range(1,len(nums)):
        if nums[i]>=nums[i-1]:
            dp[i] =dp[i-1]+1
        else:
            dp[i]= dp[i-1]
    print(dp)
    return dp[-1]


findlongestincreasingsequence([5, 3, 2, 4,8, 6, 7])