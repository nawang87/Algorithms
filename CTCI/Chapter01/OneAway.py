def oneAway(str1, str2):
    dp = [[0 for i in range(len(str2)+1)]for i in range(len(str1) + 1)]
    # print(dp)
    m = len(str1)
    n = len(str2)
    for i in range(1, m+1):
        for j in range(1,n+1):
            # print(i,j)
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]= 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    return dp[m][n]==1

print(oneAway('pale','pbla'))
