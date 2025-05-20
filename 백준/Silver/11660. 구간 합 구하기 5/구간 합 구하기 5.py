from sys import stdin as input
n,m = map(int,input.readline().split())
dp = [[0] + list(map(int,input.readline().split())) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(1,n+1):
        dp[i][j] += dp[i][j-1]
for _ in range(m):
    x1,y1,x2,y2 = map(int,input.readline().split())
    x1 -= 1
    x2 -= 1
    s = 0
    for i in range(x1,x2+1):
        s += dp[i][y2] - dp[i][y1-1]
    print(s)