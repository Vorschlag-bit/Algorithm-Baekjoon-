from sys import stdin as input
n,k = map(int,input.readline().split())
arr = []
dp = [0]*(k+1)
dp[0] = 1
for _ in range(n):
    arr.append(int(input.readline().strip()))
for c in arr:
    for i in range(c,k+1):
        dp[i] += dp[i-c]
print(dp[k])