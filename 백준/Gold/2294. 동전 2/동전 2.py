from sys import stdin as input
n,k = map(int,input.readline().split())
arr = []
dp = [float('inf')]*(k+1)
dp[0] = 0
for _ in range(n):
    arr.append(int(input.readline().strip()))
arr.sort()
for i in range(1,k+1):
    for j in arr:
        if j > i: break
        dp[i] = min(dp[i],dp[i-j]+1)
print(dp[k]) if dp[k] != float('inf') else print(-1)