from sys import stdin as input
import math
def sqrt(n):
    return int(math.sqrt(n))+1
n = int(input.readline())
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = min(dp[i-j*j]+1 for j in range(1,sqrt(i)))
print(dp[n])