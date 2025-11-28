from sys import stdin as input

n,l,r = map(int,input.readline().split())

# 빌딩 높이는 1~n
# dp[i][j][k] -> i = 현재 건물의 개수, j = l에 보이는 건물 수, k = r에서 보이는 건물 수
dp = [[[0] * (r+1) for _ in range(l+1)] for _ in range(n+1)]
dp[1][1][1] = 1

# dp[i][j][k] = (dp[i-1][j-1][k] + dp[i-1][j][k-1]) * dp[i-1][j][k]
for i in range(2,n+1):
    for j in range(1,l+1):
        for k in range(1,r+1):
            dp[i][j][k] = ((dp[i-1][j-1][k] + dp[i-1][j][k-1]) + dp[i-1][j][k] * (i-2)) % 1000000007

print(dp[n][l][r])