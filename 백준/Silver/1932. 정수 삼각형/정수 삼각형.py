from sys import stdin as input
n = int(input.readline())
dp = [list(map(int,input.readline().split())) for _ in range(n)]
for i in range(1,n):
    dp[i][0] += dp[i-1][0]
    dp[i][i] += dp[i-1][i-1]
for i in range(2,n):
    for j in range(1,i):
        dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[n-1]))