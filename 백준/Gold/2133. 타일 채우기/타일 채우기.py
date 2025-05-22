n = int(input())
dp = [0]*(n+1)
dp[0] = 1
if n == 1:
    print(0)
    exit()
dp[2] = 3
if n == 2:
    print(dp[2])
    exit()
for i in range(3,n+1):
    if i % 2 == 1: continue
    dp[i] = dp[i-2]*3
    for j in range(i-4,-1,-2):
        dp[i] += dp[j]*2
print(dp[n])