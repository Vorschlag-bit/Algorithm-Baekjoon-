n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(1,k+1):
        for x in range(i+1):
            dp[i][j] += dp[i-x][j-1]
print(dp[n][k]%1000000000)