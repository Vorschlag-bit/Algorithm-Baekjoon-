from sys import stdin as input
t = int(input.readline())
for _ in range(t):
    n = int(input.readline())
    s = [list(map(int,input.readline().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
        continue
    dp[0][1] = dp[1][0] + s[0][1]
    dp[1][1] = dp[0][0] + s[1][1]
    if n == 2:
        print(max(dp[1][1],dp[0][1]))
        continue
    for j in range(2,n):
        dp[0][j] = max(dp[1][j-1],dp[1][j-2]) + s[0][j]
        dp[1][j] = max(dp[0][j-1],dp[0][j-2]) + s[1][j]
    print(max(dp[0][-1],dp[1][-1]))