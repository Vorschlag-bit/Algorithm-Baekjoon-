from sys import stdin as input
n = int(input.readline())

arr = []

for _ in range(n):
    a,b = map(int,input.readline().split())
    arr.append((a,b))

# dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱했을 때의 최소 연산 횟수
dp = [[0] * n for _ in range(n)]

# 작은 구간부터 큰 구간으로 interval DP하기 위한 구조
for gap in range(1,n):
    for start in range(n-gap):
        end = start + gap

        dp[start][end] = float('inf')

        for k in range(start,end):
            cost = dp[start][k] + dp[k+1][end] + (arr[start][0] * arr[k][1] * arr[end][1])
            dp[start][end] = min(dp[start][end], cost)

print(dp[0][n-1])