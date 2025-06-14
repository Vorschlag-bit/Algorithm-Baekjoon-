def solution(n):
    dp = [0]*(n+1)
    if n == 1: return 0
    if n == 2: return 3
    dp[0] = 1
    dp[2] = 3
    # 6 -> dp[4]*3 + dp[2]*2 = 33 + 6 = 39
    # 8 => dp[6]*3 + dp[4]*2 + dp[2]*2
    for i in range(3,n+1):
        if i%2 == 1: continue
        dp[i] = (dp[i-2]*3)%1000000007
        for j in range(i-4,-1,-2):
            dp[i] = (dp[i] + dp[j]*2)%1000000007
    return dp[n]