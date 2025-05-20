from sys import stdin as input
s1 = ['']+list(map(str,input.readline().strip()))
s2 = ['']+list(map(str,input.readline().strip()))
n = len(s1)
m = len(s2)
dp = [[0]*m for _ in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[n-1][m-1])