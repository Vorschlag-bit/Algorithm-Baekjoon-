from sys import stdin as input
n,k = map(int,input.readline().split())
bag = [list(map(int,input.readline().split())) for _ in range(n)]
dp = [[0]*(k+1)for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = bag[i-1]
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])