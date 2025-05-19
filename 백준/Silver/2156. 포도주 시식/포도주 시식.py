from sys import stdin as input
n = int(input.readline())
wine = [0]
for _ in range(n):
    wine.append(int(input.readline()))
dp = [0]*(n+1)
# dp[i] => i만 마시거나(dp[i-2] + wine[i])
dp[1] = wine[1]
if n > 1: dp[2] = dp[1] + wine[2]
for i in range(3,n+1):
    c1 = dp[i-3] + wine[i-1] + wine[i]
    c2 = dp[i-1]
    c3 = dp[i-2] + wine[i]
    dp[i] = max(c1,c2,c3)
print(dp[n])