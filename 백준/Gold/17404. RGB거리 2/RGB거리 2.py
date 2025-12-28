from sys import stdin as input

n = int(input.readline())

# 0 = r, 1 = g, 2 = b
cost = []
for _ in range(n):
    cost.append(list(map(int, input.readline().split())))

# 1번 집은 2번과 n번과 같아선 안 된다.
# i번 째 집은 i-1,i+1과 같아선 안 된다.
ans = float('inf')
for i in range(3):
    # 1번집을 i로 고정
    dp = [[0] * 3 for _ in range(n)]
    for j in range(3): dp[0][j] = float('inf')
    dp[0][i] = cost[0][i]
    # dp[j] = min(dp[j-1])
    for j in range(1,n):
        # 0
        dp[j][0] = cost[j][0] + min(dp[j-1][1],dp[j-1][2])
        # 1
        dp[j][1] = cost[j][1] + min(dp[j-1][0],dp[j-1][2])
        # 2
        dp[j][2] = cost[j][2] + min(dp[j-1][0],dp[j-1][1])
    for k in range(3):
        if k != i:
            ans = min(dp[n-1][k], ans)

print(ans)