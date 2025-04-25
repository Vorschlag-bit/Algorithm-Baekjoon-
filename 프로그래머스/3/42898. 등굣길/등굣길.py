def solution(m, n, pud):
    ans = 0
    dp = [[0] * m for _ in range(n)]
    for j,i in pud:
        dp[i-1][j-1] = -1
    dp[0][0] = 1
    for i in range(1,n):
        if dp[i][0] == -1: continue
        dp[i][0] = dp[i-1][0]
    for j in range(1,m):
        if dp[0][j] == -1: continue
        dp[0][j] = dp[0][j-1]
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != -1:
                a = 0 if dp[i-1][j] == -1 else dp[i-1][j]
                b = 0 if dp[i][j-1] == -1 else dp[i][j-1]
                dp[i][j] = a + b
                
    return dp[n-1][m-1] % 1000000007