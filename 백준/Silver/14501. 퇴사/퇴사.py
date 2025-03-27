n = int(input())

arr = [0]

for i in range(n):
    t,p = map(int, input().split())
    arr.append((t,p))

dp = [0] * (n+1)

for i in range(1,n+1):
    Ti,Pi = arr[i][0],arr[i][1]
    if Ti - 1 + i <= n:
        dp[Ti-1+i] = dp[i-1] + Pi if dp[i-1] + Pi > dp[Ti-1+i] else dp[Ti-1+i]
    dp[i] = dp[i-1] if dp[i-1] > dp[i] else dp[i]
print(dp[n])