from sys import stdin as input

n,m = map(int,input.readline().split())

# 메모리 바이트를 저장할 배열(idx = app)
size = [0] + list(map(int,input.readline().split()))
# 앱을 비활성화할 때 오버헤드(idx = app)
cost = [0] + list(map(int,input.readline().split()))

max_cost = sum(cost)
# dp[i][c] = i번째 어플을 고려해서 얻을 수 있는 최대의 메모리
dp = [[0]*(max_cost+1) for _ in range(n+1)]
ans = float('inf')
for i in range(1,n+1):
    for c in range(max_cost+1):
        dp[i][c] = dp[i-1][c]
        if c >= cost[i]:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-cost[i]]+size[i])
        if dp[i][c] >= m:
            ans = min(ans,c)
print(ans)